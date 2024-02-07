class Solution {
    public int solution(int angle) {
        int answer = 0;
        switch(angle){
            case 90: answer = 2; break;
            case 180: answer = 4; break;
            default:
                if(angle<90){
                    answer = 1;
                }else{
                    answer = 3;
                }
                break;
        }
        
        return answer;
    }
}