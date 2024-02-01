class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {0,0};
        int gcd = 0;
        
        if(denom1 == denom2){
            answer = new int [] {numer1 + numer2 , denom1};
        }
        else{
            answer = new int [] {numer1*denom2 + numer2*denom1 , denom1*denom2};
        }
        if(answer[0]>answer[1]){
                gcd = Euclidean(answer[0], answer[1]);
            }
            else{
                gcd = Euclidean(answer[1], answer[0]);
            }
            answer[0] = answer[0]/gcd;
            answer[1] = answer[1]/gcd;
        return answer;
    }
    int Euclidean(int a, int b) {
        if (b == 0) return a;
        return Euclidean(b, a % b);
    }   
}