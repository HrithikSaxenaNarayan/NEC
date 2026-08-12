import java.util.*;

public class lec10 {
    public static Scanner scn = new Scanner(System.in);

    public static void newfunc() {
        String str = "";
        long start = System.currentTimeMillis();
        for (int i = 0; i < (int) 1e5; i++) {
            str += i;
        }
        long end = System.currentTimeMillis();
        System.out.println(end - start);
    }

    public static void stringBuilderTimeMeasure() {
        StringBuilder sb = new StringBuilder();

        long start = System.currentTimeMillis();
        for (int i = 0; i < (int) 1e6; i++) {
            sb.append(i);
        }
        long end = System.currentTimeMillis();
        System.out.println(end - start);
    }

    public static void stringBuilderOps() {
        StringBuilder sb = new StringBuilder();
        sb.append('a');
        sb.append('b').append("cdefgh ijk"); // O(m) m is the length of the existing string.
        
        System.out.println(sb);
        System.out.println(sb.toString()); // O(n) of .toString();

        sb.setCharAt(4, '7'); // O(1).
        System.out.println(sb.toString());

        sb.deleteCharAt(4); // O(n) if it is any character in the string except last character. complexity of last character is -> O(1);
        System.out.println(sb.toString());

    }
    public static void main(String[] args) {
        stringBuilderOps();
    }
}