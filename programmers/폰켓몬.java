import java.util.*;
class 폰켓몬 {
    public int solution(int[] nums) {
        Set<Integer> hash = new HashSet<Integer>();

        for(int num : nums) {
            hash.add(num);
        }
        if (hash.size() > nums.length / 2) {
            return nums.length / 2;
        } else {
            return hash.size();
        }

    }
}
