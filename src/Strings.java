import java.util.Scanner;

public class Strings {

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter First Name: ");
        String fname = sc.nextLine();
        System.out.println("Enter Last Name: ");
        String lname = sc.nextLine();
        String fullName = fname + lname;

        //charat
        for(int i=0; i<fullName.length(); i++){
            System.out.println(fullName.charAt(i));
        }

        //compare
        if(fname.compareTo(lname)==0){
            System.out.println("Equal Strings");
        } else {
            System.out.println("Diff Strings");
        }

        //Reverse
        for(int l=fullName.length() -1; l>=0; l--){
            System.out.println(fullName.charAt(l));
        }
    }
}
