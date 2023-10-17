import java.util.*;

public class 다른비트 {

    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        
        // 짝수일 경우는 +1
        // 홀수일 경우는 뒤에서 부터 0을 찾고 거기에 1을 더한 이진수가 제일 작은 수
        for (int i = 0; i<numbers.length; i++) {
            long result = numbers[i];
            String target = Long.toBinaryString(numbers[i]);
            
            if (result % 2 == 0) {
                answer[i] = result + 1;
            } else {
                int idx = target.lastIndexOf("0");
                
                if (idx == -1) {
                    String tmp = "10" + target.substring(1, target.length());
                    answer[i] = Long.parseLong(tmp, 2);
                } else {
                    String tmp = target.substring(0, idx) + "10" + target.substring(idx + 2, target.length());
                    answer[i] = Long.parseLong(tmp, 2);
                }
            }
            
            
//             while (true) {
//                 result++;
                
//                 String binaryString = Long.toBinaryString(result);
                
//                 int cnt = 0;
//                 if (target.length() != binaryString.length()) {
//                     target = "0" + target;  
//                 } 
                
//                 for (int j = 0; j<binaryString.length(); j++) {
//                         if (binaryString.charAt(j) != target.charAt(j)) {
//                             cnt++;
//                         }
//                 }
                
                
//                 if (cnt == 1 || cnt == 2) {
//                     break;
//                 }
//             }
            
//             answer[i] = result;
        }
        return answer;
    }
}
