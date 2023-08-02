import java.util.*;
class 이진변환반복하기 {
    public int[] solution(String s) {
        int[] answer = new int[2];
        String target = s;
        int rst = s.length();
        // 해당 반복문을 탐색
        while (true) {
            int cnt = 0;
            for(int i=0; i<target.length(); i++) {
                if (target.charAt(i)=='0') {
                    cnt++; // 0 count
                }
            }
            answer[0]++;
            answer[1] += cnt;
            rst -= cnt;

            if (rst==1) {
                break;
            }
            // 다시 이진수로 변환
            target = Integer.toBinaryString(rst);
            rst = target.length();
        }
        return answer;
    }
}
