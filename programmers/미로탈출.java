import java.util.*;

class 미로탈출 {
    class Node {
        int x;
        int y;
        int cnt;
        
        public Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
    
    char[][] arr;
    boolean[][] visited;
    
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public int bfs(int ci, int cj, int n, int m, char target) {
        Queue<Node> que = new LinkedList<Node>();
        que.add(new Node(ci, cj, 0));
        visited[ci][cj] = true;
        
        while (!que.isEmpty()) {
            Node node = que.poll();
            
            if (arr[node.x][node.y] == target) {
                return node.cnt;
            }
            
            for (int d = 0; d<4; d++) {
                int nx = node.x + dx[d];
                int ny = node.y + dy[d];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (!visited[nx][ny] && arr[nx][ny] != 'X') {
                        que.add(new Node(nx, ny, node.cnt + 1));
                        visited[nx][ny] = true;
                    }
                }
                
            }
            
        }
        return -1;
    }
    
    public int solution(String[] maps) {
        int answer = 0;
        arr = new char[maps.length][maps[0].length()];
        visited = new boolean[maps.length][maps[0].length()];
        
        int si = 0, sj = 0, li = 0, lj = 0, ei = 0, ej = 0;
        
        // 2차원 배열
        for (int i = 0; i<maps.length; i++) {
            String str = maps[i];
            for (int j = 0; j<maps[0].length(); j++) {
                if (str.charAt(j) == 'S') {
                    si = i;
                    sj = j;
                } else if (str.charAt(j) == 'L') {
                    li = i;
                    lj = j;
                } else if (str.charAt(j) == 'E') {
                    ei = i;
                    ej = j;
                }
                arr[i][j] = str.charAt(j);
            }
        }
        
        int result1 = bfs(si, sj, maps.length, maps[0].length(), 'L');
        
        if (result1 == -1) {
            return -1;
        }
        
        visited = new boolean[maps.length][maps[0].length()];
        int result2 = bfs(li, lj, maps.length, maps[0].length(), 'E');
        
        if (result2 == -1) {
            return -1;
        }
        
        return result1 + result2;
    }
}