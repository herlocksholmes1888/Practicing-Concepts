public class Main {
  public static void main(String[] args) {
    int[] Fibonacci = new int[10];

    Fibonacci[0] = 0;
    Fibonacci[1] = 1;

    for (int i = 2; i < Fibonacci.length; i++) {
      Fibonacci[i] = Fibonacci[i - 1] + Fibonacci[i - 2];
    }

    for (int i = 2; i < Fibonacci.length; i++) {
      System.out.println(Fibonacci[i]);
    }
  }
}