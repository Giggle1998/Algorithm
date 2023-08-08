import java.util.*;

class 점프와순간이동 {
    public int solution(int n) {
        int ans = 0;
        while(n > 0) {
            // Top-Down 방식으로 2로 나누어지고 나머지가 0인 경우에만 탐색 진행
            if (n / 2 > 0 && n % 2 == 0) {
                n /= 2;
            } else {
                n--;
                ans++;
            }
        }

        return ans;
    }
}
