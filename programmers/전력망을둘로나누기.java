import java.util.*;

class 전력망을둘로나누기 {
    static int[][] arr;
    public int solution(int n, int[][] wires) {
        int answer = n;
        arr = new int[n + 1][n + 1];

        for (int i=0; i<wires.length; i++) {
            arr[wires[i][0]][wires[i][1]] = 1;
            arr[wires[i][1]][wires[i][0]] = 1;
        }

        for (int i=0; i<wires.length; i++) {
            arr[wires[i][0]][wires[i][1]] = 0;
            arr[wires[i][1]][wires[i][0]] = 0;

            answer = Math.min(answer, bfs(n, wires[i][0]));

            arr[wires[i][0]][wires[i][1]] = 1;
            arr[wires[i][1]][wires[i][0]] = 1;
        }

        return answer;
    }
    public int bfs(int n, int s) {
        Queue<Integer> que = new LinkedList<>();
        que.offer(s);
        boolean[] visited = new boolean[n+1];
        visited[s] = true;
        int cnt = 1;

        while (!que.isEmpty()) {
            int c = que.poll();

            for (int i=1; i<=n; i++) {
                if (visited[i]) {
                    continue;
                }
                if (arr[c][i] == 1) {
                    que.offer(i);
                    visited[i] = true;
                    cnt++;
                }
            }
        }
        return (int)Math.abs(n - 2*cnt);
    }
}
