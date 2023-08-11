import java.util.*;

class 멀리뛰기 {
    public long solution(int n) {
        long[] answer = new long[2001];
        answer[1] = 1;
        answer[2] = 2;
        answer[3] = 3;

        for (int i=4; i<2001; i++) {
            answer[i] = (answer[i-1] + answer[i-2]) % 1234567;
        }
        return answer[n];
    }
}
