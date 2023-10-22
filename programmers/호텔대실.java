import java.util.*;

public class 호텔대실 {
    public int solution(String[][] book_time) {
        int answer = 0;
        int[][] bookTime = new int[book_time.length][2];
        
        for (int i = 0; i<book_time.length; i++) {
            int start = Integer.parseInt(book_time[i][0].replace(":", ""));
            int end = Integer.parseInt(book_time[i][1].replace(":", ""));
            
            end += 10; // 청소 시간
            
            if (end % 100 == 60) {
                end += 40;
            }
            
            bookTime[i][0] = start;
            bookTime[i][1] = end;
            
        }
        
        System.out.println(Arrays.deepToString(bookTime));
        
        return answer;
    }
}
