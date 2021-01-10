import java.lang.Math;

class Solution {
    public int reverse(int x) {
        int reversed = 0;
        String givenNum = "" + x;
        int power; 
        if(x < 0){ power = givenNum.length() - 2;}else{power = givenNum.length() - 1;}  
    
        while(x != 0){
            reversed += x%10 * Math.pow(10, power);
            x = x/10;
            power -= 1;
        }
        if(reversed == 2147483647 || reversed == -2147483648 ){return 0;}
        
        return reversed;
    }
}
