import java.util.*;

class 괄호회전하기 {
    public int solution(String s) {
        int answer = 0;

        for (int i = 0; i<s.length(); i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(s.substring(i));
            sb.append(s.substring(0, i));
            Stack<Character> stk = new Stack<Character>();
            for (char c : sb.toString().toCharArray()) {
                if (stk.isEmpty()) {
                    stk.push(c);
                } else {
                    if (c == '}' && stk.peek() == '{') {
                        stk.pop();
                    } else if(c== ']' && stk.peek() == '[') {
                        stk.pop();
                    } else if(c== ')' && stk.peek() == '(') {
                        stk.pop();
                    } else {
                        stk.push(c);
                    }
                }
            }
            if (stk.size() == 0) {
                answer++;
            }
        }
        return answer;
    }
}
