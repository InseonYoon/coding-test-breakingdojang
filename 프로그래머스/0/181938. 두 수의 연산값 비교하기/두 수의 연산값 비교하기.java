class Solution {
    public int solution(int a, int b) {
        String ab = "" + a + b;
        return Integer.parseInt(ab) >= (2 * a * b)?
                Integer.parseInt(ab) : 2 * a * b;
    }
}