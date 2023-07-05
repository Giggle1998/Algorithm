import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_14501 {

    static int N;
    static int[][] arr;
    static int[] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        dp = new int[N + 1];
        arr = new int[N + 1][N + 1];
        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int T = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            arr[i][0] = T;
            arr[i][1] = P;
        }

        for (int i = 1; i <= N; i++) {
            int next = i + arr[i][0] - 1;
            if (next <= N) {
                dp[next] = Math.max(dp[next], arr[i][1] + dp[i - 1]);
            }
            dp[i] = Math.max(dp[i], dp[i - 1]);
        }
        System.out.println(dp[N]);
    }

}