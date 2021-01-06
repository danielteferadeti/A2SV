
public class Sorting {

    public static void main(String[] args) {
        // TODO code application logic here
         int[] intArray = new int[]{ 1,1,3,3,5,6,7,8,9,100};
         intArray = selectionSort(intArray);
         
         String a = "";
         for (int i = 0; i < intArray.length; i++){
            a += " " + intArray[i];
        }
        System.out.println(a);
    }
    public static int[] selectionSort(int[] givenArray){
        int[] intArray = givenArray;
        int countIndex = 0;
        int indexToSwap=0;
        for(int i = 0; i < intArray.length; i++){
            int minValue = intArray[i];
            for(int j = i; j < intArray.length; j++){
                if(minValue >= intArray[j]){
                    minValue = intArray[j];
                    indexToSwap = j;
                }
            }
            int temp = intArray[countIndex];
            intArray[countIndex] = intArray[indexToSwap];
            intArray[indexToSwap] = temp;
            countIndex +=1;
        }
        return intArray;
    }
}