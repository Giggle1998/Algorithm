import java.util.*;
class 타겟넘버 {
    static int cnt = 0;
    public int solution(int[] numbers, int target) {
        int answer = 0;
        ArrayList<Integer> rst = new ArrayList<>();
        dfs(numbers, rst, 0, target);
        answer = cnt;
        return answer;
    }
    static void dfs(int[] lst, ArrayList<Integer> rst, int len, int target) {
        if (len == lst.length) {
            int sum = 0;
            for (int num : rst) {
                sum += num;
            }
            if (sum == target) {
                cnt++;
            }
            return;
        }
        rst.add(lst[len]);
        dfs(lst, rst, len+1, target);
        rst.remove(rst.size() - 1);

        rst.add(lst[len]*-1);
        dfs(lst, rst, len+1, target);
        rst.remove(rst.size() - 1);
    }
}
