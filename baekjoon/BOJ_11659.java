import java.io.*;
import java.util.*;

class BOJ_11659 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1 = br.readLine();
        StringTokenizer st1 = new StringTokenizer(line1, " ");

        int n  = Integer.parseInt(st1.nextToken());
        int m = Integer.parseInt(st1.nextToken());

        int[] prefixSum = new int[n+1];
        String line2 = br.readLine();
        StringTokenizer st2 = new StringTokenizer(line2, " ");
        for (int i = 1; i<=n; i++) {
            prefixSum[i] = prefixSum[i-1] + Integer.parseInt(st2.nextToken());
        }

        for (int k = 0 ; k<m; k++) {
            String line3 = br.readLine();
            StringTokenizer st3 = new StringTokenizer(line3, " ");
            
            int i = Integer.parseInt(st3.nextToken());
            int j = Integer.parseInt(st3.nextToken());

            System.out.println(prefixSum[j] - prefixSum[i-1]);
        }
    }
}