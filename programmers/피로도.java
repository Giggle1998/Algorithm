import java.util.*;
class 피로도 {
    static boolean[] check;
    static int cnt = -1;
    public int solution(int k, int[][] dungeons) {
        check = new boolean[dungeons.length];
        dfs(dungeons, 0, k);

        return cnt;
    }
    static void dfs(int[][] dungeons, int n, int k) {

        for (int i=0; i<dungeons.length; i++) {
            if (check[i] == false && k >= dungeons[i][0]) {
                check[i] = true;
                dfs(dungeons, n+1, k-dungeons[i][1]);
                check[i] = false;
            }
        }
        cnt = Math.max(cnt, n);
    }
}
