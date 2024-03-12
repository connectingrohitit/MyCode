public class Factorial {
    public static int factorial(int n) {
        if(n==1){
            return 1;
        }
        int fact_nm1 = factorial(n-1);
        int fact_n = n * fact_nm1;
        return fact_n;

    }
    public static void main(String[] args) {
        System.out.println(factorial(5));
    }
}
