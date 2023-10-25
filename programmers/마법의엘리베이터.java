import java.util.*;

class Ev {
    int now;
    int depth;
    Ev(int now, int depth) {
        this.now = now;
        this.depth = depth;
    }
}
public class 마법의엘리베이터 {
    public int bfs(int storey) {
        Queue<Ev> q = new LinkedList<>();
        q.add(new Ev(storey, 0));        
        int result = 10000000;
        while(!q.isEmpty()) {
            Ev ev = q.poll();
            int now = ev.now;
            int level = ev.depth;
            if(now == 0) {
                if(result > level)
                {
                    result = level;
                }
                continue;
            }
            int num = now % 10;
            if(num > 5) { //5보다 크면 걍 반올림
                q.add(new Ev(now / 10 + 1, level + 10 - num));
            }
            else if(num == 5) {
                q.add(new Ev(now / 10, level + num)); //내림
                q.add(new Ev(now / 10 + 1, level + 10 - num)); //반올림
            }
            else {
                q.add(new Ev(now / 10, level + num));                
            }
        }
        return result;
    }
    public int solution(int storey) {
        int answer = bfs(storey);
        return answer;
    }
}
