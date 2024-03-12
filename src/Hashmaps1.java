import java.util.HashMap;
import java.util.Map;

public class Hashmaps1 {
    public static void main(String[] args) {
        //Creation - Country , population
        HashMap<String, Integer> map = new HashMap<>();

        //Insertion
        map.put("India", 120);
        map.put("US", 30);
        map.put("China", 150);

        System.out.println(map);

        //search
        if(map.containsKey("India")){
            System.out.println(map.get("India"));
        }

        //remove
        map.remove("China");

        //Iterator
//        for(String val : map.keySet()){
//            System.out.println(map.get(val));
//        }

        for(Map.Entry<String, Integer> e : map.entrySet()){
            System.out.println(e.getKey());
            System.out.println(e.getValue());
        }

    }
}
