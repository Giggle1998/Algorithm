public class 스킬트리 {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for (String tree : skill_trees) {
            StringBuilder sb = new StringBuilder();
            for (char c : tree.toCharArray()) {
                if (skill.indexOf(c) != -1) {
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
