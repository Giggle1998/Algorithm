import java.util.*;

class PCCP기출2번 {
    static boolean[][] visited;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int n;
    static int m;
    static int cnt;
    
    class Node {
        int x;
        int y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public void bfs(int i, int j, int[][] land) {
        Queue<Node> que = new LinkedList<Node>();
        que.add(new Node(i, j));
        visited[i][j] = true;
        
        while (!que.isEmpty()) {
            Node node = que.poll();
            
            for (int k = 0; k<4; k++) {
                int ni = dx[k] + node.x;
                int nj = dy[k] + node.y;
                
                if (0 <= ni && ni < n && 0 <= nj && nj < m) {
                    if (visited[ni][nj] == false && land[ni][nj] == 1) {
                        visited[ni][nj] = true;
                        cnt++;
                        que.add(new Node(ni, nj));
                    }
                }
            }
            
        }
        
    }
    
    public int solution(int[][] land) {
        int answer = -1;
        n = land.length;
        m = land[0].length;

        for (int j = 0; j<m; j++) {
            visited = new boolean[n][m];
            int tmp = 0;
            for (int i = 0; i<n; i++) {
                if (land[i][j] == 1 && visited[i][j] == false) {
                    cnt = 1;
                    bfs(i, j, land);
                    tmp += cnt;
                    cnt = 0;
                }
            }
            answer = Math.max(answer, tmp);
        }

        return answer;
    }
}