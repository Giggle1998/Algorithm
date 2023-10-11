import java.util.*;

public class 방문길이 {
    public int solution(String dirs) {
        int answer = 0;
        int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("U", dir[0]);
        map.put("D", dir[1]);
        map.put("R", dir[2]);
        map.put("L", dir[3]);
        System.out.println(map.entrySet());
        int cx = 0, cy = 0;
        for (char c : dirs.toCharArray()) {
            System.out.println(c);
            
            Object d = map.get(c);
            System.out.println(d);
        }
        
        return answer;
    }
}
