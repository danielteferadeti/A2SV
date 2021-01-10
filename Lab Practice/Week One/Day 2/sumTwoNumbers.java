public class sumTwoNumbers {
    public int[] twoSum(int[] nums, int target) {
        int[] indicesArray = new int[2];
        boolean found = false;
        
        for(int i=0; i < nums.length; i++){
            for(int j=i+1; j < nums.length; j++){
                if(nums[i] + nums[j] == target){
                    indicesArray[0] = i;
                    indicesArray[1] = j;
                    found = true;
                    break;
                }
            }
            if(found){
                break;
            }
        }
        
        return indicesArray;
    }

}
