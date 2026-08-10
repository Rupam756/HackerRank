import java.util.*;

class Solution {

    public ArrayList<Boolean> processQueries(
            int[] arr,
            int[][] queries) {

        int n = arr.length;

        int[] inc = new int[n];
        int[] dec = new int[n];

        /*
         * inc[i] = ending index of the
         * non-decreasing segment starting at i
         */
        inc[n - 1] = n - 1;

        for (int i = n - 2; i >= 0; i--) {

            if (arr[i] <= arr[i + 1]) {
                inc[i] = inc[i + 1];
            } else {
                inc[i] = i;
            }
        }

        /*
         * dec[i] = starting index of the
         * non-increasing segment ending at i
         */
        dec[0] = 0;

        for (int i = 1; i < n; i++) {

            if (arr[i - 1] >= arr[i]) {
                dec[i] = dec[i - 1];
            } else {
                dec[i] = i;
            }
        }

        ArrayList<Boolean> ans = new ArrayList<>();

        for (int[] query : queries) {

            int l = query[0];
            int r = query[1];

            // Mountain condition
            ans.add(inc[l] >= dec[r]);
        }

        return ans;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna