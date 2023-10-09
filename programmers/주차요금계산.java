import java.util.*;

public class 주차요금계산 {
/*
** HashMap을 통해 차에 대한 사용 시간 정리
** 그 후 HashMap을 탐색하고 해당시간에 대한 연산 진행
*/
// 추후 다시 풀기
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        Map<String, Integer> map1 = new HashMap<String, Integer>();
        Map<String, Integer> map2 = new HashMap<String, Integer>();
        
        int baseTime = fees[0];
        int baseFee = fees[1];
        int partTime = fees[2];
        int partFee = fees[3];
        
        for (String record : records) {
            String[] tmp = record.split(" ");
            int time = getRealTime(tmp[0]);
            String car = tmp[1];
            String io = tmp[2];
            
            if (io.equals("IN")) {
                map1.put(car, time);
            } else {
                int carTime1 = map1.get(car);
                map1.remove(car);
                if (map2.containsKey(car)) {
                    int carTime2 = map2.get(car);
                    map2.replace(car, carTime2 + time - carTime1);    
                } else {
                    map2.put(car, time - carTime1);
                }   
            }
        }
        int lastTime = 1439;
        for (String car : map1.keySet()) {
            System.out.println(car);
            int carTime1 = map1.get(car);
            if (map2.containsKey(car)) {
                    int carTime2 = map2.get(car);
                    map2.replace(car, carTime2 + lastTime - carTime1);    
                } else {
                    map2.put(car, lastTime - carTime1);
            }   
        }
        System.out.println(map2.entrySet());
        Object[] sortKey = map2.keySet().toArray();	//차 번호 순서대로 정렬
		Arrays.sort(sortKey);
        answer = new int[sortKey.length];

        System.out.println(Arrays.toString(sortKey));
        
        
        return answer;
    }
    
    public int getRealTime(String time) {
        String[] tmp = time.split(":");
        int hour = Integer.parseInt(tmp[0]) * 60;
        int minute = Integer.parseInt(tmp[1]);
        return hour + minute;
    }
}
