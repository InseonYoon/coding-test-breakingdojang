class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        long product = 1;
        
        for(int i: num_list){
            sum += i;
            product *= Long.valueOf(i);
        }
        
        return product < sum*sum ? 1 : 0;
    }
}