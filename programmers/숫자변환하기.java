import java.util.*;

class Solution {
    static int a;
    static int b;
    static int c;
    static int answer = 1000000;
    public int solution(int x, int y, int n) {
        a = x;
        b = y;
        c = n;
        
        dfs(b, 0);
        
        if (answer == 1000000) {
            answer = -1;
        }
        return answer;
    }
    
    public void dfs(int target, int cnt) {
        if (target < a) {
            return;
        }
        
        if (target == a) {
            answer = Math.min(cnt, answer);
            return;
        }
        
        int ncnt = cnt + 1;
        int target1 = target - c;
        int target2 = target / 2;
        int target3 = target / 3;
        
        dfs(target1, ncnt);
        if (target % 2 == 0) {
            dfs(target2, ncnt);    
        }
        if (target % 3 == 0) {
            dfs(target3, ncnt);    
        }
        
    }
}
