import java.util.*;

class 이중우선순위큐 {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer> pq1 = new PriorityQueue<Integer>();
        PriorityQueue<Integer> pq2 = new PriorityQueue<Integer>(Collections.reverseOrder());
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        for (String str : operations) {
            String[] tmp = str.split(" ");
            
            if (tmp[0].equals("I")) {
                pq1.add(Integer.parseInt(tmp[1]));
                pq2.add(Integer.parseInt(tmp[1]));
            } else {
                if (pq1.size() > 0 || pq2.size() > 0) {
                    if (tmp[1].equals("1")) {
                        int max = pq2.poll(); // 최댓값 삭제
                        pq1.remove(max);
                    } else {
                        int min = pq1.poll(); // 최솟값 삭제
                        pq2.remove(min);
                    }
                }
            }
        }
        
        if (!pq1.isEmpty()) {
            answer[0] = pq2.peek();
            answer[1] = pq1.peek();
        }
        
        return answer;
    }
}