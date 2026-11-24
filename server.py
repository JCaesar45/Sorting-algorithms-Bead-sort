import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "server" / "waitlist.json"
LOCK = threading.Lock()
EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def load():
    try:
        return json.loads(DB.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return []


class Handler(BaseHTTPRequestHandler):
    def reply(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.reply(200, (ROOT / "index.html").read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/health":
            self.reply(200, {"ok": True})
        else:
            self.reply(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/waitlist":
            return self.reply(404, {"error": "not found"})
        size = int(self.headers.get("Content-Length") or 0)
        if not 0 < size <= 2048:
            return self.reply(400, {"error": "bad size"})
        try:
            email = str(json.loads(self.rfile.read(size)).get("email", "")).strip().lower()
        except (json.JSONDecodeError, AttributeError):
            return self.reply(400, {"error": "bad json"})
        if not EMAIL.match(email):
            return self.reply(400, {"error": "invalid email"})
        with LOCK:
            entries = load()
            if email in entries:
                return self.reply(409, {"error": "exists"})
            entries.append(email)
            DB.write_text(json.dumps(entries, indent=2))
        self.reply(201, {"ok": True})


if __name__ == "__main__":
    print("http://localhost:8000")
    ThreadingHTTPServer(("", 8000), Handler).serve_forever()
