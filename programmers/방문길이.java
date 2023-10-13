import java.util.*;

class 방문길이 {
    public int solution(String dirs) {
        int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        Map<Character, int[]> map = new HashMap<Character, int[]>();
        List<int[]> visited = new ArrayList<int[]>();
        map.put('U', dir[0]);
        map.put('D', dir[1]);
        map.put('R', dir[2]);
        map.put('L', dir[3]);

        int cx = 0, cy = 0;
        for (char c : dirs.toCharArray()) {
            int[] d = map.get(c);
            boolean check = false;
            if (cx + d[0] > 5 || cx + d[0] < -5 || cy + d[1] > 5 || cy + d[1] < -5) {
                continue;
            }
            
            int[] visit = {cx, cy, cx + d[0], cy + d[1]};
            cx += d[0];
            cy += d[1];
            for (int[] v : visited) {
                if (Arrays.equals(v, visit) || Arrays.equals(v, new int[]{visit[2], visit[3], visit[0], visit[1]})) {
                    check = true;
                    break;
                }
            }
            
            if (check) {
                continue;
            }
            
            visited.add(visit);
        }

        return visited.size();
    }
}