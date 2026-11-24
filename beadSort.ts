export function beadSort(input: readonly number[]): number[] {
  if (!input.every((n) => Number.isInteger(n) && n > 0)) {
    throw new RangeError("beadSort expects positive integers");
  }
  if (input.length === 0) return [];
  const poles: number[] = new Array<number>(Math.max(...input)).fill(0);
  for (const n of input) for (let i = 0; i < n; i++) poles[i]++;
  const out: number[] = [];
  for (let row = 0; row < input.length; row++) {
    let count = 0;
    for (let i = 0; i < poles.length; i++) {
      if (poles[i] > 0) {
        count++;
        poles[i]--;
      }
    }
    out.push(count);
  }
  return out.reverse();
}

if (typeof process !== "undefined" && process.argv[1]?.endsWith("beadSort.ts")) {
  console.log(beadSort([25, 32, 12, 7, 20]));
}
