import java.util.*;

public class lec2 {
    public static Scanner scn = new Scanner(System.in);

    public static void reverseOrder(int n) {
        while (n != 0) {
            int ans = n % 10;
            System.out.println(ans);
            n /= 10;
        }
    }

    public static int power(int n) {
        int pow = 1;
        while (n != 0) {
            n /= 10;
            pow *= 10;
        }
        return pow / 10;
    }

    public static void forwardOrder(int n) {
        int pow = power(n);
        while(n != 0) {
            int ans = n / pow;
            System.out.println(ans);
            n %= pow;
            pow /= 10;
        }
    }
    public static void main(String[] args) {
        forwardOrder(scn.nextInt());
    }
}
