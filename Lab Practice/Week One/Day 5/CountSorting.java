
public class Sorting {

    public static void main(String[] args) {
        // TODO code application logic here
         int[] intArray = new int[]{ 1,1,3,3,5,6,7,8,9,100};
         intArray = countingSorting(intArray);
         
         String a = "";
         for (int i = 0; i < intArray.length; i++){
            a += " " + intArray[i];
        }
        System.out.println(a);
    }
    
    public static int[] countingSorting(int[] givenArray){
        int[] intArray = givenArray;
        int maxNum = intArray[0];
        int[] countingArray;
        int indexCount = 0;
        
        for (int i = 0; i < intArray.length; i++){
            if(maxNum < intArray[i]){
                maxNum = intArray[i];
            }
        }
        countingArray = new int[maxNum + 1];
        for (int i = 0; i < intArray.length; i++){
            countingArray[intArray[i]] +=1;
        }
        
        for (int i = 0; i < countingArray.length; i++){
            if(countingArray[i]!=0){
                for(int j =0; j<countingArray[i] ; j++){
                    intArray[indexCount]= i;
                    indexCount +=1;
                }
            }  
        }
        
        return intArray;
    }
    
}
