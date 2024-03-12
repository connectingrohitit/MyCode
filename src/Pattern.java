public class Pattern {
    public static void main(String args[]){
        printPattern(5);
        printPyramid(5);
        printUltaPyramid(6);
    }
    private static void printPattern(int rows){
        for(int i=1; i<=rows; i++)
        {
            for(int j = 1; j<=i; j++)
            {
                System.out.print(" *");
            }
            System.out.println();
        }

    }

    private static void printPyramid(int row){
        for(int i = 1; i<=row ; i++)
        {
            for(int j = row; j>=i; j--)
            {
                System.out.print(" ");
            }
            for(int k=1; k<=i; k++){
                System.out.print(" *");
            }
            System.out.println();

        }
    }

    private static void printUltaPyramid(int row){
        for(int i = 1; i<=row ; i++)
        {
            for(int j = row; j>=i; j--)
            {
                System.out.print(" *");
            }

            System.out.println();

            for(int k=1; k<=i; k++){
                System.out.print(" ");
            }
        }
    }
}
