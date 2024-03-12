//Search for a given number x in 2Darray
import java.util.Scanner;

public class TwoDArray {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter count of rows: ");
        int rows = sc.nextInt();
        System.out.println("Enter count of columns: ");
        int cols = sc.nextInt();

        //define 2D array
        int[][] num = new int[rows][cols];

        //inputs
        System.out.println("Enter items of 2D array: ");
        for(int i=0; i<rows;i++){
            for(int j=0; j<cols; j++){
                num[i][j] = sc.nextInt();
            }
        }

        //Take X input
        System.out.println("Enter searchable value 'X': ");
        int x = sc.nextInt();

        //output
        for(int i=0; i<rows;i++){
            for(int j=0; j<cols; j++){
                if(num[i][j] == x){
                    System.out.println("'X' found at index : " + i +"," +j + " i.e. row no: " + (i+1) + "& column no:"+ (j+1));
                }
            }
        }


    }
}
