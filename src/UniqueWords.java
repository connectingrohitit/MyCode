import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.stream.Stream;

public class UniqueWords {
    public static void main(String args[]){
        String str = "Selenium was originally developed by Jason Huggins in 2004 as an internal tool at ThoughtWorks. " +
                "Huggins was later joined by other programmers and testers at ThoughtWorks, before Paul Hammant joined the team and steered the development of the second mode of operation that would later become \"Selenium Remote Control\" (RC). The tool was open sourced that year.\n" +
                "\n";
        String refStr = str.replace(".","").replace(",","").replace("\"", "");
        String refinedStr[] = refStr.split(" ");

        HashMap<String, Integer> unique = new HashMap<String, Integer>();
        for (String str2: refinedStr) {
            if(unique.get(str2)== null)
            {
                unique.put(str2, 1);
            }
            else
                unique.put(str2, unique.get(str2)+1);

        }
        System.out.println(unique);

        System.out.println("The max entry is: " + getMaxEntryInMapBasedOnValue(unique));


        /*HashSet<String> uniqueWords = new HashSet<String>(Arrays.asList(refinedStr));
        for (String s:
             uniqueWords) {
            System.out.println(s);*/

        }

    public static <K, V extends Comparable<V> >
    Map.Entry<K, V>
    getMaxEntryInMapBasedOnValue(Map<K, V> map)
    {

        // To store the result
        Map.Entry<K, V> entryWithMaxValue = null;

        // Iterate in the map to find the required entry
        for (Map.Entry<K, V> currentEntry :
                map.entrySet()) {

            if (
                // If this is the first entry, set result as
                // this
                    entryWithMaxValue == null

                            // If this entry's value is more than the
                            // max value Set this entry as the max
                            || currentEntry.getValue().compareTo(
                            entryWithMaxValue.getValue())
                            > 0) {

                entryWithMaxValue = currentEntry;
            }
        }

        // Return the entry with highest value
        return entryWithMaxValue;
    }
    }
