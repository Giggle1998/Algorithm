import java.util.*;

public class 두큐합같게만들기 {
    static long getSum(int[] arr) {
        long rst = 0;
        for (int i = 0; i<arr.length; i++) {
            rst += arr[i];
        }
        
        return rst;
    }
    
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for (int i = 0; i<queue1.length; i++) {
            q1.add(queue1[i]);
            q2.add(queue2[i]);
        }
        
        long sum1 = getSum(queue1);
        long sum2 = getSum(queue2);
        
        while (sum1 != sum2) {
            if (answer > (queue1.length + queue2.length) * 2) {
                return -1;
            }
            
            if (sum1 > sum2) {
                int tmp = q1.poll();
                q2.add(tmp);
                sum1 -= tmp;
                sum2 += tmp;
            } else if (sum1 < sum2) {
                int tmp = q2.poll();
                q1.add(tmp);
                sum2 -= tmp;
                sum1 += tmp;
                
            }
            answer++;
        }        
        return answer;
    }
}
