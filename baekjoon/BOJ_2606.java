import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2606 {

    static int N, M, cnt;
    static int[][] graph;
    static boolean[] check;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        N = Integer.valueOf(st1.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        M = Integer.valueOf(st2.nextToken());

        graph = new int[N + 1][N + 1];
        check = new boolean[N + 1];
        for (int i = 0; i < M; i++) {
            StringTokenizer st3 = new StringTokenizer(br.readLine());
            int v1 = Integer.valueOf(st3.nextToken());
            int v2 = Integer.valueOf(st3.nextToken());
            graph[v1][v2] = graph[v2][v1] = 1;
        }
        bfs(1);
        System.out.println(cnt);
    }

    public static void bfs(int v) {
        Queue<Integer> que = new LinkedList<>();
        que.add(v);
        check[v] = true;

        while (!que.isEmpty()) {
            Integer num = que.poll();
            if (num != 1) {
                cnt += 1;
            }
            for (int i = 1; i <= N; i++) {
                if (graph[num][i] == 1 && !check[i]) {
                    check[i] = true;
                    que.add(i);
                }
            }
        }
    }

}