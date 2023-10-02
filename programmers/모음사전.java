import java.util.*;

public class 모음사전 {
    static List<String> list = new ArrayList<>();
    static String[] alpha = {"A", "E", "I", "O", "U"};
    public int solution(String word) {
        int answer = 0;
        dfs("", 0);
        
        for(int i = 0; i<list.size(); i++) {
            if (list.get(i).equals(word)) {
                answer = i;
                break;
            }
        }
        return answer;
    }
    
    public void dfs(String str, int len) {
        list.add(str);
        if (len == 5) return;
        for (int i = 0; i < 5; i++) {
            dfs(str + alpha[i], len + 1);
        }   
    }
}

