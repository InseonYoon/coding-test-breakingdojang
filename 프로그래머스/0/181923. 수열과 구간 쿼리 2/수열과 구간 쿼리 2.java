class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for(int j=0; j<queries.length; j++){
            answer[j] = 1_000_001;
            for(int i = queries[j][0]; i <= queries[j][1]; i++){
                if(arr[i] > queries[j][2]){
                    answer[j] = (answer[j] > arr[i])? arr[i]: answer[j];
                }
            }
            if(answer[j] == 1_000_001){
                answer[j] = -1;
            }
        }
        return answer;
    }
}