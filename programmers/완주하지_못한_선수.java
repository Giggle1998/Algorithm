import java.util.*;
class 완주하지_못한_선수 {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i=0; i<completion.length; i++){
            // 동명이인이 아닌 경우 정답 처리
            if(!participant[i].equals(completion[i])){
                return participant[i];
            }
        }
        // 마지막 인물이 정답처리
        return participant[participant.length-1];
    }
}
