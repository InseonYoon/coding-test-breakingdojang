class Solution {
    public String solution(String code) {
        int mode = 0;
        char[] codeArr = code.toCharArray();
        StringBuilder sb = new StringBuilder();
        
        for(int idx = 0; idx < codeArr.length; idx++){
            switch(mode){
                case 0:
                    if(codeArr[idx] == '1'){
                        mode = 1;
                    }else{
                        if(idx%2 == 0){
                            sb.append(codeArr[idx]);
                        }                       
                    }
                    break;
                    
                case 1:
                    if(codeArr[idx] == '1'){
                        mode = 0;
                    }else{
                        if(idx%2 == 1){
                            sb.append(codeArr[idx]);
                        }                       
                    }
                    break;
            }
        }
        
        return sb.toString().isEmpty()? "EMPTY": sb.toString();
    }
}