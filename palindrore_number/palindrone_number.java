class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false
        }
        
        String xStr = Integer.toString(x);
        String reverseStr = "";
        int reverse_x;

        for (int i = xStr.length() - 1; i >= 0; i-- ) {
            reverseStr += xStr.charAt(i);
        }

        try{
            reverse_x = Integer.valueOf(reverseStr);
        }catch(Exception e){
            return false;
        }

        if (reverse_x == x) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        System.out.println(solution.isPalindrome(10));

    }
}