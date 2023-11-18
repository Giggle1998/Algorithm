import java.util.*;

class 숫자카드나누기 {
    // 두 번 탐색 A, B
    // 만족하는 값이 없다면 0 or 만족한다면 제일 큰 수 반환
    
    /* 
    ** 1. 제일 작은 값 찾기
    ** 2. 작은 값의 약수 찾기
    ** 3. 해당 배열에서 나눠지는 지 탐색
    ** 4. 다른 배열에서는 나눠지지 않는지 탐색
    */ 
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        
        int rstA = 0, rstB = 0;
        int minA = 100000000;
        int minB = 100000000;
        
        for (int num : arrayA) {
            minA = Math.min(minA, num);
        }
        
        for (int num : arrayB) {
            minB = Math.min(minB, num);
        }
        
        rstA = checkCard(arrayA, arrayB, minA);
        rstB = checkCard(arrayB, arrayA, minB);
        
        answer = Math.max(rstA, rstB);
        return answer;
    }
    public int checkCard(int[] a, int[] b, int minNum) {
        for (int i = minNum; i>=2; i--) {
            if (minNum % i == 0) {
                int cnt = 0;
                for (int num : a) {
                    if (num % i == 0) {
                        cnt++;
                    }
                }
                
                if (cnt == a.length) {
                    cnt = 0;
                    for (int num : b) {
                        if (num % i != 0) {
                            cnt++;
                        }
                    }
                    
                    if (cnt == b.length) {
                        return i;
                    }
                }
            }
        }
        return 0;
    }
}
