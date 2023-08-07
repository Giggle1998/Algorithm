import java.util.*;

class 배달 {
    static int cnt = 1;
    static int[] visited;
    static class Node {
        int x, y, v;

        Node(int x, int y, int v) {
            this.x = x;
            this.y = y;
            this.v = v;
        }
    }
    public int solution(int N, int[][] road, int K) {
        ArrayList<ArrayList<Node>> lst = new ArrayList<>();
        for (int i=0; i<=N; i++) {
            lst.add(new ArrayList<>());
        }
        // 양방향 연결
        for (int[] r : road) {
            lst.get(r[0]).add(new Node(r[0], r[1], r[2]));
            lst.get(r[1]).add(new Node(r[1], r[0], r[2]));
        }
        visited = new int[N+1];
        for (int i = 2; i<visited.length; i++) {
            visited[i] = Integer.MAX_VALUE;
        }
        bfs(lst.get(1), lst, K);
        return cnt;
    }
    public void bfs(ArrayList<Node> node, ArrayList<ArrayList<Node>> lst, int K) {
        Queue<Node> que = new LinkedList<>();
        que.addAll(node);

        while (!que.isEmpty()) {
            Node n = que.poll();

            if(visited[n.y] >= visited[n.x] + n.v) {
                visited[n.y] = visited[n.x] + n.v;
                que.addAll(lst.get(n.y));
            }
        }

        for (int i=2; i<visited.length; i++) {
            if (visited[i] <= K) cnt++;
        }
    }
}
