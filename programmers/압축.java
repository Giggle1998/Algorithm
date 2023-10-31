import java.util.*;
import java.util.stream.*;

class 압축 {
    
    public int[] solution(String msg) {
        
        Queue<String> queue = new LinkedList<>();
        
        for(String word: msg.split("")) {
            queue.offer(word);
        }
        
        List<String> list = IntStream.range('A', 'Z'+1)
            .mapToObj(val -> String.valueOf((char) val))
            .collect(Collectors.toList());
        
        List<Integer> result = new ArrayList<>();
        
        String value = "";
        while(!queue.isEmpty() || !"".equals(value)) {
            if(list.contains(value + queue.peek())) {   
                value = value + queue.poll();
                continue;
            }
            
            list.add(value+queue.peek());
            result.add(list.indexOf(value)+1);
            value = "";
        }
        
        
        return result.stream()
            .mapToInt(val -> val.intValue())
            .toArray();
    }
}
