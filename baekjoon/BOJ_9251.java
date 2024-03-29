import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_9251 {
 
	static char[] str1;
	static char[] str2;
 
	static int[][] dp;
	
	static int LCS(int[][] dp) {

		for (int i = 1; i<=str1.length; i++) {
			for (int j = 1; j<=str2.length; j++) {
				// 문자가 동일한 경우 -> 이전값에 +1
				if (str1[i-1] == str2[j-1]) {
					dp[i][j] = dp[i-1][j-1] + 1;
				// 문자가 동일하지 않은 경우 -> 최대값 탐색
				} else {
					dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j]);
				}
			}
		}

		return dp[str1.length][str2.length];
	}

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		StringTokenizer st2 = new StringTokenizer(br.readLine());
 
		str1 = st1.nextToken().toCharArray();
		str2 = st2.nextToken().toCharArray();
		
		dp = new int[str1.length+1][str2.length+1];
 
		System.out.println(LCS(dp));		
	}
}