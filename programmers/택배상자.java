import java.util.*;

public class 택배상자 {
    public int solution(int[] order) {
        int answer = 0;
        
        Stack<Integer> sub = new Stack<>();
        
        int idx = 0;
        for (int num = 1; num <= order.length; num++) {
            if (order[idx] == num) {
                answer++;
                idx++;
            } else {
                sub.push(num);
            }
            
            while (!sub.isEmpty() && sub.peek() == order[idx]) {
                sub.pop();
                idx++;
                answer++;
            }
        }

        return answer;
    }
}
