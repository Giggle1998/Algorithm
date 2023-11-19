import java.util.*;

class 메뉴리뉴얼 {
    // 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문
    // 가장 많이 함께 주문된 단품메뉴 조합을 추가
    /*
    ** 1. orders를 정렬
    ** 2. order에 따른 조합 만들기
    ** 3. 가장 많은 조합을 저장
    */
    List<String> list = new ArrayList<>();
    Map<String, Integer> map = new HashMap<>();
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        
        for (int i = 0; i<orders.length; i++) {
            char[] arr = orders[i].toCharArray();
            Arrays.sort(arr);
            orders[i] = String.valueOf(arr);
        }
        
        for (int len : course) {
            for (String order : orders) {
                // 조합 만들기
                comb("", order, len);
            }
            if (!map.isEmpty()) {
                List<Integer> tmp = new ArrayList<>(map.values());
                Collections.sort(tmp);
                int maxNum = Collections.max(tmp);
                
                // 최소 2명 이상의 손님으로부터 주문
                if (maxNum > 1) {
                    for (String key : map.keySet()) {
                        if (maxNum == map.get(key)) {
                            list.add(key);
                        }
                    }
                }
            }
            map.clear();
        }
        
        
        Collections.sort(list);
        answer = new String[list.size()];
        for (int i = 0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }
        System.out.println(Arrays.toString(orders));
        return answer;
    }
    
    public void comb(String order, String sub, int cnt) {
        if (cnt == 0) {
            map.put(order, map.getOrDefault(order, 0) + 1);
            return;
        }
        
        for (int i = 0; i<sub.length(); i++) {
            comb(order + sub.charAt(i), sub.substring(i+1), cnt - 1);
        }
    }
}
