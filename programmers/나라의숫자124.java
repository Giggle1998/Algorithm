import java.util.*;

class 나라의숫자124 {
    public String solution(int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        if (n < 4) {
            if (n == 1) {
                return "1";
            } else if (n == 2) {
                return "2";
            } else {
                return "4";
            }
        }
        
        int tmp = 0;
        while (n != 0) {
            tmp = n % 3;
            n = n / 3;
            
            if (tmp == 0) {
                tmp = 4;
                n--;
            }
            
            sb.append(tmp);
        }
        
        return sb.reverse().toString();
    }
}
