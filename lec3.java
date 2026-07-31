import java.util.*;

public class lec3 {
    public static Scanner scn = new Scanner(System.in);

    public static void binomialPattern(int num) {
        for (int n = 0; n < num; n++) {
            int nCr = 1;
            for (int r = 0; r <= n; r++) {
                System.out.print(nCr + "\t");
                int nCr1 = ((n - r) * nCr) / (r + 1);
                nCr = nCr1;
            }
            System.out.println();
        }
    }

    public static void numPattern4(int n) {
        int nsp = n - 1;
        int nst = 1;

        for (int row = 1; row <= n; row++) {
            for (int csp = 1; csp <= nsp; csp++) {
                System.out.print("\t");
            }

            int val = row;
            for (int cst = 1; cst <= nst; cst++) {
                System.out.print(val + "\t");
                if (cst <= nst / 2) {
                    val++;
                } else {
                    val--;
                }
            }
            nsp--;
            nst += 2;
            System.out.println("\t");
        }
    }

    public static void main(String[] args) {
        binomialPattern(scn.nextInt());
    }
}