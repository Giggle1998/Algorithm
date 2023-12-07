import java.util.*;
import java.io.*;

/*
 * 3, 7번이 맞닿아있는 자석
 * 시계방향 1, 반시계 방향 -1
 */
public class BOJ_14891 {
    static int N = 4;
    static int[][] gear;
    static int[] top;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
        gear = new int[N+1][8];
        top = new int[N+1];

		for(int i=1; i<=4 ;i++) {
			String s = br.readLine();
			for(int j=0; j<8; j++) {
				gear[i][j] = s.charAt(j) - '0';
			}
		}
        
        int K = Integer.parseInt(br.readLine());
        for (int k = 0; k<K; k++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int idx = Integer.parseInt(st.nextToken());
            int dr = Integer.parseInt(st.nextToken());

            int[][] tlst = new int[N+1][2];
            tlst[0][0] = idx;
            tlst[0][1] = 0;

            // 우측 방향 처리
            for (int i = idx + 1; i <= N; i++) {
                if (gear[i - 1][(top[i - 1] + 2) % 8] != gear[i][(top[i] + 6) % 8]) {
                    tlst[i - idx - 1][0] = i;
                    // 0이면 같은 방향, 1이면 다른 방향
                    tlst[i - idx - 1][1] = (i - idx) % 2;
                } else {
                    break;
                }
            }

            // 좌측 방향 처리
            for (int i = idx - 1; i > 0; i--) {
                if (gear[i][(top[i] + 2) % 8] != gear[i + 1][(top[i + 1] + 6) % 8]) {
                    tlst[idx - i - 1][0] = i;
                    // 0이면 같은 방향, 1이면 다른 방향
                    tlst[idx - i - 1][1] = (idx - i) % 2;
                } else {
                    break;
                }
            }

            // 실제 회전 처리
            for (int i = 0; i < tlst.length; i++) {
                int[] lst = tlst[i];
                if (lst[1] == 0) {
                    top[lst[0]] = (top[lst[0]] - dr + 8) % 8;
                } else {
                    top[lst[0]] = (top[lst[0]] + dr + 8) % 8;
                }
            }
        }
        int ans = 0;
        int[] tbl = {0, 1, 2, 4, 8};
        for (int i = 1; i <= N; i++) {
            ans += gear[i][top[i]] * tbl[i];
        }
        System.out.println(ans);
    }
}
