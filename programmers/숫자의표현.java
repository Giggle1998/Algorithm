import java.util.*;

class 숫자의표현 {
    public int solution(int n) {
        int answer = 1;

        for(int i = 1; i<=n/2+1; i++) {
            int rst = i;
            int tmp = i+1;
            while(true) {
                rst += tmp;

                if(rst == n) {
                    answer++;
                    break;
                } else if (rst > n) {
                    break;
                } else {
                    tmp++;
                }

            }
        }
        return answer;
    }
}
