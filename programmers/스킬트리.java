import java.util.*;

public class 스킬트리 {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        List<Character> list = new ArrayList<>();
        
        for (char c : skill.toCharArray()) {
            list.add(c);
        }
        
        for (String tree : skill_trees) {
            StringBuilder sb = new StringBuilder();
            for (char c : tree.toCharArray()) {
                if (list.contains(c)) {
                    sb.append(String.valueOf(c));
                }
            }

            int cnt = 0;
            for (int i = 0; i < sb.length(); i++) {
                if (sb.charAt(i) == skill.charAt(i)) {
                    cnt++;
                }
            }
            
            if (cnt == sb.length()) {
                answer++;
            }
        }
        
        
        return answer;
    }
}
