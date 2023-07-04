import java.util.Arrays;

class 가장_큰_수 {
    public String solution(int[] numbers) {
        // [6, 10, 2]
        String answer = "";
        String[] arr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }
        System.out.println(arr);
        Arrays.sort(arr, (a1, a2) -> (a1 + a2).compareTo(a2 + a1));
        if (arr[0].equals("0")) {
            return "0";
        }
        for (String str : arr) {
            answer += str;
        }
        return answer;
    }
}
