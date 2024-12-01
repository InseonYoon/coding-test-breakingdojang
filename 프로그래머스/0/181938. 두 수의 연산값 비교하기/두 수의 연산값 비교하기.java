import java.lang.Math;

class Solution {
    public int solution(int a, int b) {
        double ab = a * Math.pow(10, (int)Math.log10(b)+1) + b;
        return (int)ab >= (2 * a * b)? (int)ab : 2 * a * b;
    }
}
