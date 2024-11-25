class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        char[] my_arr = my_string.toCharArray();
        char[] over_arr = overwrite_string.toCharArray();
        System.arraycopy(over_arr, 0, my_arr, s, over_arr.length);
        
        return new String(my_arr);
    }
}