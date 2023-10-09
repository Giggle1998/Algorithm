import java.util.*;

class 뒤에있는큰수찾기 {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        // 2중 for문은 시간초과로 불가능
        Stack<Integer> stk = new Stack<Integer>();
        
        answer[numbers.length - 1] = -1;
        int idx = 1;
        stk.push(0);
        for (int i = 1; i<numbers.length; i++) {
            
            while (!stk.isEmpty() && numbers[stk.peek()] < numbers[i]) {
                answer[stk.pop()] = numbers[i];
            }
            stk.push(i);
        }
        // System.out.println(Arrays.toString(answer));
        // System.out.println(stk);
        while (!stk.isEmpty()) {
            answer[stk.pop()] = -1;
        }
        
        return answer;
    }
}