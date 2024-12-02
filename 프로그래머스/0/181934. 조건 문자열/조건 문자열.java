class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        String ineqOri = "";
        String eqOri = "";
        
        /*
            먼저 n, m 대소비교하고
            비교 결과에 따라 ineqOri와 eqOri에 해당하는 문자열 저장
            각각 원본과 파라미터 일치여부 확인
        */
        
        if(n > m){
            ineqOri += ">";
        }else if(n < m){
            ineqOri += "<";
        }else{
            eqOri += "=";
        }
        
        return ineq.equals(ineqOri) || eq.equals(eqOri) ? 1 : 0;
    }
}