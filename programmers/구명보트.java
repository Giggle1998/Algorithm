import java.util.*;

class 구명보트 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);

        int min_idx = 0;
        int max_idx = people.length - 1;

        while (min_idx <= max_idx) {
            if (people[min_idx] + people[max_idx] <= limit) {
                answer++;
                min_idx++;
                max_idx--;

            } else {
                answer++;
                max_idx--;
            }
        }
        return answer;
    }
}
