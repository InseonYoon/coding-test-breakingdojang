class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int svs = n/10;
        answer = n*12000 + (k-svs)*2000;
        
        System.out.println(n + "인분을 시켜 서비스로 음료수를 " + svs + "개 받아 총 " + (n*12000 + (k-svs)*2000) + "원입니다.");
        
        return answer;
    }
}