import java.util.*;

class 예상대진표 {
    public int solution(int n, int a, int b)
    {
        int cnt = 0;
        while (true) {
            a = (a + 1) / 2;
            b = (b + 1) / 2;
            cnt++;

            if(a == b) {
                break;
            }
        }
        return cnt;
    }
}
