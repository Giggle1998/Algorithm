import java.util.*;

class PCCP기출1번 {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = -1;
        int time = bandage[0]; // 기술 시전 시간
        int one = bandage[1]; // 1초당 회복
        int plus = bandage[2]; // 추가 회복
        
        int maxHealth = health;
        int cur = 0;
        
        Queue<int[]> que = new LinkedList<int[]>();
        
        for (int[] attack : attacks) {
            que.add(attack);
        }
        
        int l = attacks.length;
        
        for (int i = 1; i<=attacks[l-1][0]; i++) {
            int[] tmp = que.peek();
            
            if (tmp[0] == i) {
                cur = 0;
                health -= tmp[1];
                que.poll();
                
                if (health <= 0) {
                    break;
                }
                
            } else {
                cur += 1;
                if (cur == time) {
                    health += plus;
                    cur = 0;
                }
                health += one;
                
                if (health >= maxHealth) {
                    health = maxHealth;
                }
            }
            
        }
        
        if (health > 0) {
            answer = health;
        }
        
        return answer;
    }
}