import java.util.*;
// 뉴스 클러스터링 코드
class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int target = 65536;
        
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        
        List<String> lst1 = divide(str1);
        List<String> lst2 = divide(str2);
        List<String> set1 = new ArrayList<>();
        List<String> set2 = new ArrayList<>();
        
        Collections.sort(lst1);
        Collections.sort(lst2);
        
        for (String s : lst1) {
            if (lst2.remove(s)) {
                set1.add(s);
            }
            set2.add(s);
        }
        
        for (String s : lst2) {
            set2.add(s);
        }
        // 교집합이랑 합집합이 0일때
        if (set1.size() == 0 && set2.size() == 0) {
            return target;
        }
        
        double rst = (double) set1.size() / (double) set2.size();
        
        
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