import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1697 {
    static int N;
    static int K;
    static int[] check = new int[100001];
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        N = scan.nextInt();
        K = scan.nextInt();

        if (N == K) {
            System.out.println(0);
        } else {
            bfs(N);
        }
    }

    static void bfs(int num) {
        Queue<Integer> que = new LinkedList<>();
        que.add(num);
        check[num] = 1;

        while (!que.isEmpty()) {
            int tmp = que.poll();

            for (int i = 0; i < 3; i++) {
                int next;

                if (i == 0) {
                    next = tmp + 1;
                } else if (i == 1) {
                    next = tmp - 1;
                } else {
                    next = tmp * 2;
                }

                if (next == K) {
                    System.out.println(check[tmp]);
                    return;
                }
                if (next >= 0 && next < check.length && check[next] == 0) {
                    que.add(next);
                    check[next] = check[tmp] + 1;
                }
            }
        }
    }

}