import java.util.*;

public class 더맵게 {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int num : scoville) {
            pq.add(num);
        }
        
        while (true) {
            if (pq.peek() >= K) {
                break;
            }
            
            if (pq.size() < 2) {
                return -1;
            }
            
            int num1 = pq.poll();
            int num2 = pq.poll();
            int tmp = num1 + (num2 * 2);
            pq.add(tmp);
            answer++;            
        }
        return answer;
    }    
}
