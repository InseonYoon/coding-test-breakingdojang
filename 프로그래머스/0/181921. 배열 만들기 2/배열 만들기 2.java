import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> result = new ArrayList<>();
        
        for(int i=0; i<64; i++){
            String binary = Integer.toBinaryString(i);
            String numStr = binary.replace('1', '5');
            int num = Integer.parseInt(numStr);
            
            if(num >= l && num <=r){
                result.add(num);
            }
        }
        
        if(result.isEmpty()){
            return new int[]{-1};
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
