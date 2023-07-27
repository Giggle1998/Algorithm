import java.util.*;

class 단어변환 {
    static boolean[] check;
    static int cnt = 987654321;
    public int solution(String begin, String target, String[] words) {
        int answer = 0;

        check = new boolean[words.length];
        dfs(check, 0, begin, target, words);

        if (cnt==987654321) {
            answer = 0;
        } else {
            answer = cnt;
        }

        return answer;
    }
    public void dfs(boolean[] check, int rst, String cur, String end, String[] words) {
        if (cur.equals(end)) {
            cnt = Math.min(cnt, rst);
            return;
        }

        for (int i=0; i<words.length; i++) {
            if (!check[i]) {
                int tmp = 0;
                check[i] = true;
                for (int j=0; j<words[i].length(); j++) {
                    if (words[i].charAt(j)!=cur.charAt(j)) {
                        tmp++;
                    }
                }
                if (tmp==1) {
                    dfs(check, rst+1, words[i], end, words);
                }
                check[i] = false;

            }
        }
    }
}
