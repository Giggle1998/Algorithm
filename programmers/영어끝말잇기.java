import java.util.*;

class 영어끝말잇기 {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        ArrayList<String> lst = new ArrayList<>();
        int n1 = 0; // 몫
        int n2 = 0; // 나머지
        for (int i=0; i<words.length; i++) {
            n1 = i / n;
            n2 = i % n;
            if (lst.size() != 0){
                String before = lst.get(lst.size() - 1);
                if (lst.contains(words[i]) || before.charAt(before.length() - 1) != words[i].charAt(0)) {
                    answer[0] = n2 + 1;
                    answer[1] = n1 + 1;
                    break;
                }
            }
            lst.add(words[i]);
        }

        return answer;
    }
}
