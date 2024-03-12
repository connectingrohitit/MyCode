import java.util.ArrayList;
import java.util.Collections;

public class ArrayLists {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(0);
        list.add(2);
        list.add(3);

        //insert
        list.add(1, 1);


        //read
        System.out.println(list);

        //set
        list.set(0, 5);

        System.out.println(list);

        //get size
        System.out.println(list.size());


        //Sort list
        Collections.sort(list);
        System.out.println(list);

    }
}
