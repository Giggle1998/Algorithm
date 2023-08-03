import java.util.*;

class 다음큰숫자 {
    public int solution(int n) {
        int answer = 0;

        String target = Integer.toBinaryString(n);
        int cnt = 0;
        for (int i=0; i<target.length(); i++) {
            if (target.charAt(i) == '1') {
                cnt++;
            }
        }

        int rst = n+1;
        while (true) {
            String brst = Integer.toBinaryString(rst);
            int bcnt = 0;

            for (int i=0; i<brst.length(); i++) {
                if (brst.charAt(i) == '1') {
                    bcnt++;
                }
            }

            if (cnt == bcnt && rst > n) {
                answer = rst;
                break;
            }
            rst++;
        }

        return answer;
    }
}
