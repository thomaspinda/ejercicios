public class Fb {
    public static void main(String[] args) {
      int i=0;
      while(i!=100){
        i++;
        if(i%3== 0 && i%5==0){
          System.out.println("fizzbuzz");
        }
        else if(i%3==0){
          System.out.println("fizz");
        }
        else if (i%5==0) {
          System.out.println("buzz");
        }
        else if(i%3!=0 && i%5!=0){
          System.out.println(i);
        }
      }
    }
  }