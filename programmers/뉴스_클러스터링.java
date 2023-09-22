import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int target = 65536;
        
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        
        List<String> lst1 = divide(str1);
        List<String> lst2 = divide(str2);
        HashSet<String> set = new HashSet<String>();
    
        int cnt1 = 0; // 교집합                          
        int cnt2 = 0; // 합집합
        for (String s1 : lst1) {
            for (String s2 : lst2) {
                if (s1.equals(s2)) {
                    cnt1++;
                    break;
                }
            }
        }
        if (lst1.size() == 0 && lst2.size() == 0) {
            return target;
        }
        
        cnt2 = lst1.size() + lst2.size() - cnt1;
        double rst = (double) cnt1 / (double) cnt2;
        
        
        answer = (int) (rst * target);
        return answer;
    }
    
    public List<String> divide(String str) {
        List<String> lst = new ArrayList<>();
        
        for (int i = 0; i<str.length() - 1; i++) {
            String tmp = "";
            char c1 = str.charAt(i);
            char c2 = str.charAt(i+1);
            
            if (c1 >= 'A' && c1 <= 'Z') {
                tmp += c1;
            }
            if (c2 >= 'A' && c2 <= 'Z') {
                tmp += c2;
            }
            
            if (tmp.length() > 1) {
                lst.add(tmp);
            }
            
        }
        return lst;
    }
}