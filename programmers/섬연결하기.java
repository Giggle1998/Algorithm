import java.util.*;

class 섬연결하기 {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int[] land = new int[n];

        for (int i=0; i < n; i++) {
            land[i] = i;
        }

        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));

        for(int i=0; i < costs.length; i++) {
            if (find(land, costs[i][0]) != find(land, costs[i][1])) {
                union(land, costs[i][0], costs[i][1]);
                answer += costs[i][2];
            }
        }

        return answer;
    }

    public int find(int[] land, int n) {
        if (land[n] == n) {
            return n;
        }
        return find(land, land[n]);
    }

    public void union(int[] land, int i, int j) {
        int x = find(land, i);
        int y = find(land, j);
        land[x] = y;
    }
}
