import java.util.Scanner;
public class BOJ_1024 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int L = scanner.nextInt();

        while (true) {
            int min = N / L - ((L - 1) / 2);
            if (min < 0 || L > 100) {
                System.out.println(-1);
                System.exit(0);
            }
            int sum = (min * 2 + L - 1) * L / 2;
            if (sum == N) {
                for (int i = 0; i < L; i++) {
                    System.out.print((min+i) + " ");
                }
                System.exit(0);
            }
            L++;
        }

    }
}