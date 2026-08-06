import java.util.*;
public class lec6{
    public static Scanner scn = new Scanner(System.in);

        public static int[] input(int n){
        int[] arr = new int[n] ;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = scn.nextInt();
        }
        return arr;
    }

    public static void display(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + "\t");
        }
        System.out.println();
    }
    

    public static int[] oddLeftEvenRyt(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 != 0) {
                arr[i] *= -1;
            }
        }

        Arrays.sort(arr);

        // for (int i = 0; i < arr.length; i++) {
        //     if (arr[i] < 0) {
        //         arr[i] *= -1;
        //     }
        // }

        int idx = 0;
        while(arr[idx] < 0) {
            arr[idx] *= -1;
            idx++;
        }

        return arr;
    }

    public static void main(String[] args){
        display(oddLeftEvenRyt(input(scn.nextInt())));
    }
}

// 6 3 9 0 4 2 10 8 7