import java.util.*;

class 캐시 {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) return cities.length * 5;

        int answer = 0;

        LinkedList<String> cache = new LinkedList<>();

        for (String city : cities) {
            String s = city.toUpperCase();

            if(cache.remove(s)) {
                answer += 1;
            } else {
                answer += 5;
                if (cache.size() >= cacheSize) {
                    cache.remove(0);
                }
            }
            cache.add(s);
        }
        return answer;
    }
}
