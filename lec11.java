import java.util.Scanner;
import java.util.ArrayList;
public class lec11 {

    public static Scanner scn = new Scanner(System.in);

    public static void arrayLstOps() {
        ArrayList<Integer> arrLst = new ArrayList<>();
        // set or adding elements in the arrayList
        arrLst.add(10);
        arrLst.add(scn.nextInt());
        arrLst.add(scn.nextInt());
        arrLst.add(40);
        System.out.println(arrLst);

        // to know the length of arrayList, default size is 15 of arrayList and it will
        // vary
        arrLst.size();

        // get or render on particular element
        arrLst.get(2); // index we have to provide in the parenthesis to get an element.

        // looping on arrayLst
        for (Integer i = 0; i < arrLst.size(); i++) {
            System.out.println(arrLst.get(i));
        }
        // or
        for (Integer elem : arrLst) {
            System.out.print(elem + "\t");
        }

        // to remove or delete element from array list
        arrLst.remove(2);
    }

    public static void main(String[] args) {
        
    }
}
