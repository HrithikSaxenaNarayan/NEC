import java.util.*;
public class lec8{
    public static Scanner scn = new Scanner(System.in);

    public static boolean palindromeString(String str, int si, int ei){
        boolean isPalindrome = false;
        while(si < ei) {
            if (str.charAt(si) == str.charAt(ei)) {
                isPalindrome = true;
            }
            si++;
            ei--;
        }
        return isPalindrome;
    }

    public static void main(String[] args){
    // System.out.println(palindromeString(scn.nextLine()));
    }
}