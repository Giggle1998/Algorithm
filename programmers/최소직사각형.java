import java.util.*;
class 최소직사각형 {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxH = 0;
        int maxW = 0;
        for (int[] size : sizes) {
            if (size[0] < size[1]) {
                int tmp = size[0];
                size[0] = size[1];
                size[1] = tmp;
            }
            if (maxH < size[1]) {
                maxH = size[1];
            }
            if (maxW < size[0]) {
                maxW = size[0];
            }
        }
        answer = maxH * maxW;
        return answer;
    }
}
