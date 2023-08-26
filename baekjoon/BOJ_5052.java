import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 트라이 구조로 저장하여 완성된 문자열의 수와 전화번호 목록의 수를 비교하여
 * 두 개의 수가 동일하다면 일관성이 있는 경우이고 아니라면 일관성이 없다.
 */
public class BOJ_5052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i<T; i++) {
            Trie trie = new Trie();
            boolean flag = true;
            int N = Integer.parseInt(br.readLine());

            for (int j = 0; j < N; j++) {
                // 일관성 있는 문자열이라면 true 반환 or 일관성 없는 문자열 false 반환
                if (!trie.insert(br.readLine())) {
                    flag = false;
                }
            }

            if (flag) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }

    }
    static class TrieNode {
        // Trie의 자식 노드들은 해시맵으로 구성
        HashMap<Character, TrieNode> childNodes = new HashMap<>();
        // 문자열의 마지막 여부를 확인하기 위한 변수
        boolean isLast;
    }

    static class Trie {
        // 문자열의 root 노드, 하나만 존재
        TrieNode root = new TrieNode();

        boolean insert(String number) {
            TrieNode thisNode = root;
            for (int i = 0; i<number.length(); i++) {
                char c = number.charAt(i);
                // 해당 문자가 없으면 노드 추가
                if (thisNode.childNodes.get(c) == null) {
                    thisNode.childNodes.put(c, new TrieNode());
                }
                // 현재 위치한 노드로 이동
                thisNode = thisNode.childNodes.get(c);
                // 만약 현재 노드까지 동일했던 문자열이 마지막이라면 일관성이 없는 경우 -> false 반환
                if (thisNode.isLast) {
                    return false;
                }
             }
            // 문자열 탐색 후에도 자식노드가 존재한다면 일관성이 없는 경우 -> false 반환
            if (thisNode.childNodes.size() != 0) {
                return false;
            }
            // 현재까지 도달하면 일관성 있는 경우 -> true 반환
            thisNode.isLast = true;
            return true;
        }
    }

}