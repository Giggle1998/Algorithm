import java.util.*;

public class 무인도여행 {
    char[][] arr;
    boolean[][] visited;
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    static PriorityQueue<Integer> result = new PriorityQueue<>();
    
    class Node {
        int x;
        int y;
        
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public void bfs(int ci, int cj) {
        Queue<Node> que = new LinkedList<Node>();
        que.add(new Node(ci, cj));
        visited[ci][cj] = true;
        
        int sum = Character.getNumericValue(arr[ci][cj]);
        
        while (!que.isEmpty()) {
            Node node = que.poll();
            
            for (int i = 0; i<4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                if (nx >= 0 && nx < arr.length && ny >= 0 && ny < arr[0].length) {
                    if (arr[nx][ny] != 'X' && visited[nx][ny] == false) {
                        visited[nx][ny] = true;
                        que.add(new Node(nx, ny));
                        sum += Character.getNumericValue(arr[nx][ny]);
                    }
                }
            }
            
        }
        result.add(sum);
    }
    
    public int[] solution(String[] maps) {
        int[] answer = {};
        arr = new char[maps.length][maps[0].length()];
        visited = new boolean[maps.length][maps[0].length()];
        
        for (int i = 0; i<maps.length; i++) {
            for (int j = 0; j<maps[i].length(); j++) {
                arr[i][j] = maps[i].charAt(j);
            }
        }
        
        for (int i = 0; i<arr.length; i++) {
            for (int j = 0; j<arr[0].length; j++) {
                if (arr[i][j] != 'X' && visited[i][j] == false) {
                    bfs(i, j);
                }
            }
        }
        
        if (result.isEmpty()) {
            result.add(-1);
        }
        answer = new int[result.size()];
        for (int i = 0; i<answer.length; i++) {
            answer[i] = result.poll();
        }
        return answer;
    }
    
}
