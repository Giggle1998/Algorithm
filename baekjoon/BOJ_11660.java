import java.util.*;
import java.io.*;


class BOJ_11660 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] prefixSum = new int[n+1][n+1];

        for (int i = 1; i<=n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 1; j<=n; j++) {
                prefixSum[i][j] = prefixSum[i][j-1] + Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i<m; i++) {
            int sum = 0;
            st = new StringTokenizer(br.readLine(), " ");
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            for (int j = x1; j<=x2; j++) {
                sum = sum + (prefixSum[j][y2] - prefixSum[j][y1-1]);
            }
            sb.append(sum + "\n");
        }
        System.out.println(sb);
    }
}