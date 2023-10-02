import java.util.*;

class 숫자변환하기 {
    public int solution(int x, int y, int n) {
        int answer = 0;
        
        Queue<Integer> que = new LinkedList<Integer>();
        Set<Integer> visited = new HashSet<Integer>();
        
        que.add(x);
        visited.add(x);
        
        while (!que.isEmpty()) {
            int size = que.size();
            
            for (int i = 0; i < size; i++) {
                int num = que.poll();
            
                if (num == y) {
                    return answer;
                }
                if (num + n <= y && !visited.contains(num + n)) {
                    que.add(num + n);
                    visited.add(num + n);
                }
                if (num * 2 <= y && !visited.contains(num * 2)) {
                    que.add(num * 2);
                    visited.add(num * 2);
                }
                if (num * 3 <= y && !visited.contains(num * 3)) {
                    que.add(num * 3);
                    visited.add(num * 3);
                }
                
            }
            answer++;
            
        }
        
        return -1;
    }
}