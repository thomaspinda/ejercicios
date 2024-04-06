public class Fibonacci {
    public static void main(String[] args) {
        int x = 0;
        int y = 1;

        do{
            System.out.println(x);
            int fib = x + y;
            x = y;
            y = fib;

        }while(x<50);
    }
}