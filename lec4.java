import java.util.*;
public class lec4{
    public static Scanner scn = new Scanner(System.in);

    public static int decimalToBinary(int n) {
        int ans = 0;
        int pow = 1;
        while (n != 0) {
            int rem = n % 2;
            n /= 2;
            ans += rem * pow;
            pow *= 10;
        }
        return ans;
    }

    public static int binaryToDecimal(int n) {
        int pwr = 1;
        int ans = 0;
        while (n != 0) {
            int rem = n % 10;
            ans += rem * pwr;
            pwr *= 2;
            n /= 10;
        }
        return ans;

    }

    public static void main(String[] ARGS) {
        decimal to binary(scn.nextInt());
    }
}