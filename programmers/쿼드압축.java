public class 쿼드압축 {
    static int[] answer;
    
    public boolean check(int[][] arr, int x, int y, int len, int target) {
        for (int i = x; i<x+len; i++) {
            for (int j = y; j<y+len; j++) {
                if (arr[i][j] != target) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public void quad(int[][] arr, int x, int y, int len) {
        
        if (check(arr, x, y, len, arr[x][y])) {
            if (arr[x][y] == 0) {
                answer[0]++;
            } else {
                answer[1]++;
            }
            return;
        }
        
        quad(arr, x, y, len / 2);
        quad(arr, x + len / 2, y, len / 2);
        quad(arr, x, y + len / 2, len / 2);
        quad(arr, x + len / 2, y + len / 2, len / 2);
    }
    
    
    public int[] solution(int[][] arr) {
        answer = new int[2];
        
        quad(arr, 0, 0, arr.length);
        
        return answer;
    }
}
