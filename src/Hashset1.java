import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.TreeSet;

public class Hashset1 {
    public static void main(String[] args) {
        //create
        HashSet<String> set = new HashSet<>();

        //insert
        set.add("Rohit");
        set.add("Shrivastava");
        set.add("GP");
        set.add("Pune");

        // search -- contains
//        if(set.contains(1)){
//            System.out.println(true);
//        }

        System.out.println(set);

        //remove
//        set.remove(1);
//        if(! set.contains(1)){
//            System.out.println("Removed Successfully");
//        }

        //size
        System.out.println(set.size());

        //iterator
        Iterator it = set.iterator();
        while(it.hasNext()) {
            System.out.println(it.next());
        }

        //sort
        TreeSet<String> ts = new TreeSet<>(set);
        System.out.println(ts);

    }
}
