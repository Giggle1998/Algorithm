import java.util.*;

class 단속카메라 {
    public int solution(int[][] routes) {
        int answer = 0;
        Arrays.sort(routes, (r1, r2) -> r1[1] - r2[1]);
        int cam = -30001;
        
        for (int[] route : routes) {
            if (cam < route[0]) {
                cam = route[1];
                answer++;
            }
        }
        return answer;
    }
}
