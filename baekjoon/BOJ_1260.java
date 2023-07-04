import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1260 {
    static StringBuilder sb = new StringBuilder();
    static int N, M, V;
    static int[][] graph;
    static boolean[] check;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line, " ");

        N = Integer.valueOf(st.nextToken());
        M = Integer.valueOf(st.nextToken());
        V = Integer.valueOf(st.nextToken());

        graph = new int[N+1][N +1];
        check = new boolean[N + 1];
        for (int i = 0; i < M; i++) {
            String data = br.readLine();
            StringTokenizer str = new StringTokenizer(data, " ");
            int v1 = Integer.valueOf(str.nextToken());
            int v2 = Integer.valueOf(str.nextToken());
            graph[v1][v2] = graph[v2][v1] = 1;
        }
        dfs(V);
        sb.append("\n");
        check = new boolean[N + 1];
        bfs(V);

        System.out.println(sb.toString());
    }

    private static void bfs(int v) {
        Queue<Integer> que = new LinkedList<Integer>();
        que.add(v);
        check[v] = true;

        while (!que.isEmpty()) {
            v = que.poll();

            sb.append(v + " ");

            for (int i = 1; i <= N; i++) {
                if (graph[v][i] == 1 && !check[i]) {
                    check[i] = true;
                    que.add(i);
                }
            }
        }
    }
    private static void dfs(int v) {
        sb.append(v + " ");
        check[v] = true;

        for (int i = 1; i <= N; i++) {
            if (graph[v][i] == 1 && !check[i]) {
                dfs(i);
            }
        }
    }

}