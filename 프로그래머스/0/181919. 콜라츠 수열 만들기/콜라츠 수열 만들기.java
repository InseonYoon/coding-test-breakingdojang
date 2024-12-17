import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<>();
        int x = n;
        list.add(n);
        
        while(x != 1){
            x = (x%2 == 0)? x/2 : 3*x+1;
            list.add(x);
        }
        
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}