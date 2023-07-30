import java.util.*;

class 여행경로 {
    static ArrayList<String> lst = new ArrayList<>();
    static boolean[] visited;
    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];

        dfs("ICN", "ICN", 0, tickets);

        Collections.sort(lst);
        return lst.get(0).split(" ");
    }
    static void dfs(String cur, String root, int cnt, String[][] tickets) {
        if (cnt == tickets.length) {
            lst.add(root);
            return;
        }
        for (int i=0; i<tickets.length; i++) {
            if (!visited[i] && cur.equals(tickets[i][0])) {
                visited[i] = true;
                dfs(tickets[i][1], root + " " + tickets[i][1], cnt+1, tickets);
                visited[i] = false;
            }
        }
    }
}
