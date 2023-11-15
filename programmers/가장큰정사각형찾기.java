import java.util.*;

class 가장큰정사각형찾기
{
    public int solution(int [][]board)
    {
        int answer = 0;
        
        int[][] dp = new int[board.length + 1][board[0].length + 1];
        for (int i = 1; i<=board.length; i++) {
            for (int j = 1; j<=board[0].length; j++) {
                if (board[i - 1][j - 1] != 0) {
                    int tmp = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                    dp[i][j] = tmp + 1;
                    answer = Math.max(answer, dp[i][j]);
                }
            }
        }
        return answer * answer;
    }
}
