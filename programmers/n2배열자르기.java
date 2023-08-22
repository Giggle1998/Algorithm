import java.util.*;

class n2배열자르기 {
    public int solution(int[] number) {
        int answer = 0;

        for (int i = 0; i<number.length; i++) {
            int tmp = number[i];
            for (int j = i+1; j<number.length; j++) {
                tmp += number[j];
                for (int z = j + 1; z<number.length; z++) {
                    if (tmp + number[z] == 0) {
                        answer++;
                        // break;
                    }
                }
                tmp -= number[j];
            }
        }
        return answer;
    }
}
