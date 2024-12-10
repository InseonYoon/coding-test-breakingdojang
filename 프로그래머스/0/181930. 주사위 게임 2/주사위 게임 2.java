import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        set.add(a);
        set.add(b);
        set.add(c);
        
        switch(set.size()){
            case 1:
                answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c);
                break;
            case 2:
                answer = (a + b + c) * (a*a + b*b + c*c);
                break;
            case 3:
                answer = (a + b + c);
                break;
        }
        
        return answer;
    }
}