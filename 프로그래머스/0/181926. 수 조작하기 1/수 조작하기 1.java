class Solution {
    public int solution(int n, String control) {
        int answer = n;
        char[] arr = control.toCharArray();
        for(char c: arr){
            switch(c){
                case 'w':
                    answer += 1;
                    break;
                case 's':
                    answer -= 1;
                    break;
                case 'd':
                    answer += 10;
                    break;
                case 'a':
                    answer -= 10;
                    break;
                default:
                    break;
            }
                
        }
        return answer;
    }
}