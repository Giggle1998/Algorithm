import java.util.*;
import java.io.*;

/*
-99 1 2 5 5 7 10을 중간으로 나눌 때
-99, 1, 2, 5 는 오름차순이고  5, 7, 10 은 내림차순이다.
그렇다면 오름차순된 pq에서 가장 앞 값이 정답이다.
우선순위 큐를 오름차순, 내림차순을 각각 만든후 오름차순큐와 내림차순큐 앞자리 값을 비교하여
큰값은 내림차순큐 쪽으로, 작은 값은 오름차순큐 쪽으로 변경한다.
*/
public class BOJ_1655 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minPq = new PriorityQueue<>();
        
        int[] arr = new int[N];
        for (int i = 0; i<N; i++) {
            int num = Integer.parseInt(br.readLine());

            if (maxPq.size() == minPq.size()) {
                maxPq.add(num);
            } else {
                minPq.add(num);
            }

            if (!maxPq.isEmpty() && !minPq.isEmpty()) {
                if (minPq.peek() < maxPq.peek()) {
                    minPq.add(maxPq.poll());
                    maxPq.add(minPq.poll());
                }
            }
            sb.append(maxPq.peek() + "\n");
        }
        System.out.println(sb);

    }
}