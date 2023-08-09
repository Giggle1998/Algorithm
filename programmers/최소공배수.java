import java.util.*;

class 최소공배수 {
    public int solution(int[] arr) {
        // 1. 오름차순 2. 탐색하며 유클리드 호제법으로 진행
        Arrays.sort(arr);

        for (int i=0; i<arr.length-1; i++) {
            int num = getGCD(arr[i+1], arr[i]);
            arr[i+1] = (arr[i] * arr[i+1]) / num;

        }
        return arr[arr.length-1];
    }
    // 최대 공약수 구하기
    public static int getGCD(int n1, int n2) {
        if  (n1 % n2 == 0) {
            return n2;
        }
        return getGCD(n2, n1%n2);
    }
}
