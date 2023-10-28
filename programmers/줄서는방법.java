import java.util.*;

class 줄서는방법 {
    static int[] arr;
    static boolean[] visited;
    static int[] answer;
    static List<int[]> output = new ArrayList<>();
    static int arrSize;
    
    public void permutation(int depth) {
        if (depth == arrSize) { // 3개 모두 뽑았을 경우
            // System.out.println("answer: " + Arrays.toString(answer));

            int[] dupArr = new int[arrSize];
            for (int i = 0; i < arrSize; i++) {
                dupArr[i] = answer[i];
            }

            output.add(dupArr);

            return;
        }

        for (int i = 0; i < arrSize; i++) {
            if (!visited[i]) {
                visited[i] = true;

                answer[depth] = arr[i];
                permutation(depth + 1);

                visited[i] = false;
            }
        }

    }
    
    public int[] solution(int n, long k) {
        arr = new int[n];
        visited = new boolean[n];
        answer = new int[n];
        arrSize = n;

        for (int i = 1; i <= n; i++) {
            arr[i - 1] = i;
        }

        permutation(0);


        return output.get(Integer.parseInt(String.valueOf(k - 1)));
    }
}
