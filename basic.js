function beadSort(arr) {
  const max = Math.max(...arr);
  // Matrix (1D "poles") of zeroes, one slot per level up to the largest value
  const poles = new Array(max).fill(0);

  // Drop beads: for each element, add one to every index from 0 up to that value
  for (const num of arr) {
    for (let i = 0; i < num; i++) {
      poles[i]++;
    }
  }

  // Read the beads back off: for each row, count the poles still above zero,
  // then decrease each by one
  const sorted = [];
  for (let row = 0; row < arr.length; row++) {
    let count = 0;
    for (let i = 0; i < poles.length; i++) {
      if (poles[i] > 0) {
        count++;
        poles[i]--;
      }
    }
    sorted.push(count);
  }

  // Counts come out largest-first, so reverse for ascending order
  return sorted.reverse();
}
