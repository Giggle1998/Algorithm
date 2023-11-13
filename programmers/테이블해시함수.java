import java.util.*;

class 테이블해시함수 {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data, (d1, d2) -> {
            return d1[col-1] == d2[col-1] ? d2[0] - d1[0] : d1[col-1] - d2[col-1];
        });
        
        for (int i = row_begin - 1; i < row_end; i++) {
            int sum = 0;
            for (int tmp : data[i]) {
                sum += (tmp % (i + 1));
            }
            answer ^= sum;
        }
        
        
        return answer;
    }
}