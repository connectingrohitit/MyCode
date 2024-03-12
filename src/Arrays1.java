//import java.util.*;

import java.util.Scanner;

public class Arrays1 {
    public static void main(String args[]){
        System.out.println("Enter the size: ");
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int numbers[] = new int[size];
//        int[] arr = new int[5];
//        arr[0] = 98;
//        arr[1] = 97;
//        arr[2] = 99;

        for(int i=0; i< numbers.length;i++){
            numbers[i] = sc.nextInt();
        }

        int search = sc.nextInt();

        for(int i=0; i< numbers.length;i++){
            if(numbers[i] == search) {
                System.out.println("Variable found at index : " + i);
            }
        }

    }
}
