import java.util.*;
class 베스트앨범 {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer;
        HashMap<String, Integer> allPlay = new HashMap<>();
        HashMap<String, HashMap<Integer, Integer>> allMusic = new HashMap<>();

        // 총 재생 횟수
        for (int i=0; i<genres.length; i++){
            if(!allPlay.containsKey(genres[i])){
                HashMap<Integer, Integer> map = new HashMap<>();
                map.put(i, plays[i]);
                allMusic.put(genres[i], map);
                allPlay.put(genres[i], plays[i]);
            } else {
                HashMap<Integer, Integer> map = allMusic.get(genres[i]);
                map.put(i, plays[i]);
                allMusic.put(genres[i], map);
                allPlay.put(genres[i], allPlay.get(genres[i]) + plays[i]);
            }
        }
        // 총 재생 횟수에 따른 내림차순 정렬
        List<String> lists = new ArrayList(allPlay.keySet());
        Collections.sort(lists, (s1, s2) -> allPlay.get(s2) - allPlay.get(s1));

        List<Integer> result = new ArrayList<>();
        for(String list : lists) {
            HashMap<Integer, Integer> map = allMusic.get(list);
            List<Integer> mapList = new ArrayList(map.keySet());
            // 재생횟수에 따른 인덱스 내림차순 정렬
            Collections.sort(mapList, (s1, s2) -> map.get(s2) - map.get(s1));
            result.add(mapList.get(0));
            // 가지고 있는 노래가 2개 이상이라면 추가 정답 처리
            if (mapList.size() > 1) {
                result.add(mapList.get(1));
            }
        }
        answer = new int[result.size()];
        for (int i=0; i<result.size(); i++){
            answer[i] = result.get(i);
        }

        return answer;
    }
}
