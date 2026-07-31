import java.util.*;
public class lec3{
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

    public static void main(String[] args){
        binomialPattern(scn.nextInt());
    }
}