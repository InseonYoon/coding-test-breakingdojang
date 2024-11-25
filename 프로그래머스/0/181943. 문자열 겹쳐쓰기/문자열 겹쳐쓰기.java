class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        
        /*
            문자열 배열로 바꾸고
            arraycopy로 my에 over얹고
            toString으로 다시 문자열로 바꾸기
        */
        
        char[] my_arr = my_string.toCharArray();
        char[] over_arr = overwrite_string.toCharArray();
        System.arraycopy(over_arr, 0, my_arr, s, over_arr.length);
        
        return new String(my_arr);
    }
}