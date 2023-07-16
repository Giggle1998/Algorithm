import java.util.*;
class 소수찾기 {
    static int cnt = 0;
    static HashSet<Integer> nums = new HashSet<>();
    static int[] check = {};

    public int solution(String numbers) {
        int answer = 0;
        check = new int[numbers.length()];

        dfs(numbers, check, "");

        for(int num : nums){
            primeNumber(num);
        }

        answer = cnt;
        return answer;
    }
    // 생성 가능한 숫자 만들기
    static void dfs(String numbers, int[] check, String tmp) {
        // 길이가 1이상이면 해쉬셋에 추가
        if (tmp.length() >= 1){
            int tmpNum = Integer.parseInt(tmp);
            nums.add(tmpNum);
        }

        for (int i=0; i<numbers.length(); i++){
            // 체크가 아니라면 탐색 진행
            if (check[i] == 0){
                check[i] = 1;
                tmp += numbers.charAt(i);
                dfs(numbers, check, tmp);
                tmp = tmp.substring(0, tmp.length()-1);
                check[i] = 0;
            }
        }
    }
    // 소수 찾기
    static void primeNumber(int n){
        // 0과 1은 소수가 아님
        if(n == 0) return;
        if(n == 1) return;

        // 2부터 N까지의 제곱근까지 돌면서 나누어 떨어지면 소수가 아니므로 메소드 종료.
        for(int i=2;i<=Math.sqrt(n);i++){
            if(n % i == 0) return;
        }

        // 모두 나누어 떨어지지 않으면 소수이므로 answer 증가.
        cnt++;

    }
}
