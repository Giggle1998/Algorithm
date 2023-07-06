import java.util.LinkedList;
import java.util.Queue;

class 게임_맵_최단거리 {
    static int[] Di = {1, -1, 0, 0};
    static int[] Dj = {0, 0, 1, -1};

    static class Pos{ // 큐에 들어가기위한 인자들
        int i, j, cnt;
        public Pos(int i, int j, int cnt) {
            this.i = i;
            this.j = j;
            this.cnt = cnt;
        }
    }
    public int solution(int[][] maps) {
        int answer = 0;

        int N = maps.length; // 세로
        int M = maps[0].length; // 가로
        boolean[][] check = new boolean[N][M]; // 방문체크

        Queue<Pos> que = new LinkedList<>();
        que.add(new Pos(0, 0, 0)); // 세로, 가로, 이동횟수
        check[0][0] = true;

        while(!que.isEmpty()){
            Pos cur = que.poll();
            if (cur.i==N-1 && cur.j==M-1){
                answer = cur.cnt;
                break;
            }

            for(int d=0; d<Di.length; d++){
                int ni = cur.i + Di[d];
                int nj = cur.j + Dj[d];
                // 이동 가능한 경우 큐에 추가 및 방문 체크
                if (0 <= ni && ni < N && 0 <= nj && nj < M){
                    if (maps[ni][nj] == 1 && !check[ni][nj]){
                        check[ni][nj] = true;
                        que.add(new Pos(ni, nj, cur.cnt+1));
                    }
                }
            }
        }
        if (answer == 0){
            answer = -1;
        } else {
            answer += 1;
        }

        return answer;
    }
}
