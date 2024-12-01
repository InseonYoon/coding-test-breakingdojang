import java.lang.Math;

class Solution {
    public int solution(int a, int b) {      
        double ab = a * Math.pow(10, (int)Math.log10(b)+1) + b;
        double ba = b * Math.pow(10, (int)Math.log10(a)+1) + a;
        
        return ab > ba? (int)ab : (int)ba;
    }
}