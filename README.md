# Aurum Bead

A single-file luxury landing page with a live bead-sort laboratory, a Python waitlist API, and bead sort ported to TypeScript and Java.

## Structure

```
aurum-bead/
├── index.html          HTML + CSS + JS in one file
├── server.py    stdlib HTTP server, POST /api/waitlist
├── beadSort.ts     typed implementation
├── BeadSort.java  Java implementation
└── README.md
```

## Run

```
python3 server/server.py          # http://localhost:8000
npx tsx src/beadSort.ts
javac java/BeadSort.java && java -cp java BeadSort
```

## Products

| Piece | Price |
|---|---|
| Abacus No. 1 | $4,800 |
| Pendulum | $2,350 |
| Column Cufflinks | $1,150 |

## References

Arulanandham, J. J., Calude, C. S., & Dinneen, M. J. (2002). Bead-Sort: A natural sorting algorithm. *Bulletin of the European Association for Theoretical Computer Science, 76*, 153–161.

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.
