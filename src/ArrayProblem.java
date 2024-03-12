public class ArrayProblem {
    public static int arr[] = {1,3,6,1,2,4,3};
    //public static int arr[] = {2,3,1,1,4};
    public static void main(String[] args) {

        int tempVal = 0;
        System.out.println(verifyArr(tempVal));
    }

    public static boolean verifyArr(int tempVal){
        int sizeOfArr = arr.length;
        boolean blStatus = false;
        tempVal++;

        if(tempVal == sizeOfArr -1){
            return blStatus;
        }

        if(arr[tempVal]==sizeOfArr -1 - tempVal){
            blStatus = true;
        }else{
            blStatus = verifyArr(tempVal);
        }
        return blStatus;
    }
}
