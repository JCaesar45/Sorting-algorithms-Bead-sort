import java.util.Arrays;

public final class BeadSort {
    private BeadSort() {}

    public static int[] sort(int[] input) {
        if (input.length == 0) return new int[0];
        int max = 0;
        for (int n : input) {
            if (n <= 0) throw new IllegalArgumentException("positive integers only");
            max = Math.max(max, n);
        }
        int[] poles = new int[max];
        for (int n : input) for (int i = 0; i < n; i++) poles[i]++;
        int[] out = new int[input.length];
        for (int row = 0; row < input.length; row++) {
            int count = 0;
            for (int i = 0; i < max; i++) {
                if (poles[i] > 0) { count++; poles[i]--; }
            }
            out[input.length - 1 - row] = count;
        }
        return out;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(sort(new int[] {25, 32, 12, 7, 20})));
    }
}
