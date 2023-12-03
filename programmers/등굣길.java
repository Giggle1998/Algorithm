class 등굣길 {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] arr = new int[n][m];
        
        for (int[] puddle : puddles) {
            arr[puddle[1] - 1][puddle[0] - 1] = -1; // 웅덩이가 있는 지역
        }
        arr[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == -1) {
                    arr[i][j] = 0;
                    continue;
                }
                if(i != 0) {
                    arr[i][j] += arr[i - 1][j] % 1000000007;
                }
                    
                if(j != 0) {
                    arr[i][j] += arr[i][j - 1] % 1000000007;
                }
                    
              }
                
        }
        answer = arr[n - 1][m - 1] % 1000000007;
        return answer;
    }
}
