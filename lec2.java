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

    public static void main(String[] args) {
        reverseOrder(scn.nextInt());
    }
}
