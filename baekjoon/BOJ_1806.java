import java.util.*;
import java.io.*;

// S가 될 수 있는 구간 중에 최소길이를 구하라
public class BOJ_1806 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] arr = new int[N+1];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int sum = 0, len = 0;
        int start = 0, end = 0;
        int ans = Integer.MAX_VALUE;

        while (end <= N) {
            if (sum >= S) {
                sum -= arr[start++];
                len = end - start + 1;
                if (ans > len) {
                    ans = len;
                }
            } else {
                sum += arr[end++];
            }
        }
        if (ans == Integer.MAX_VALUE) {
            System.out.println(0);
            
        } else {
            System.out.println(ans);
        }
    }
}