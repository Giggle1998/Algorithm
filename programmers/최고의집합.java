class 최고의집합 {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        
        if (n > s) {
            return new int[]{-1};
        }
        
        int quotient = s / n;
        int remainder = s % n;
        
        for (int i = 0; i < n; i++) {
            answer[i] = quotient;
        }
        
        int idx = n-1;
        for (int i = 0; i < remainder; i++) {
            answer[idx]++;
            idx--;
        }
        
        return answer;
    }
}