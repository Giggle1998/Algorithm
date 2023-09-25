import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        // hashmap 생성
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (int i=0; i<want.length; i++) {
            map.put(want[i], number[i]);
        }
        
        for (int i = 0; i < discount.length-9; i++) {
            HashMap<String, Integer> tmp = new HashMap<>(map);
            
            for (int j = i; j < i+10; j++) {
                if (tmp.containsKey(discount[j]) && tmp.get(discount[j]) > 0) {
                    int num = tmp.get(discount[j]) - 1;
                    tmp.replace(discount[j], num);
                }
            }
            
            int rst = 0;
            boolean ans = true;
            for (int value : tmp.values()) {
                rst += value;
            }
            
            if (rst == 0) {
                answer++;
            }
        }
        
        return answer;
    }
}
