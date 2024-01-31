class Solution {
    public int solution(int num1, int num2) {
        double n1 = num1;
        double n2 = num2;
        double answer = n1/n2;
        int realanswer = (int) (answer * 1000);
        
        return realanswer;
    }
}