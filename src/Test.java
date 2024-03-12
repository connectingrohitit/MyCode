import java.util.*;

class Test {
    public static void main(String[] args) {
        String s = "Selenium was originally developed by Jason Huggins in 2004 as an internal tool at ThoughtWorks. Huggins was later joined by other programmers and testers at ThoughtWorks, before Paul Hammant joined the team and steered the development of the second mode of operation that would later become 'Selenium Remote Control (RC)'. The tool was open sourced that year.In 2005 Dan Fabulich and Nelson Sproul (with help from Pat Lightbody) made an offer to accept a series of patches that would transform Selenium-RC into what it became best known for. In the same meeting, the steering of Selenium as a project would continue as a committee, with Huggins and Hammant being the ThoughtWorks representatives.";
        s = s.toLowerCase();
        s = s.replaceAll("[-+.^:,()']"," "); //Added Replace function
        HashMap<String, Integer> hm = new HashMap();
        String[] sArray = s.split(" ");
        for(int i = 0; i < sArray.length; i++){
            if(hm.containsKey(sArray[i])){
                int inc = hm.get(sArray[i]);
                hm.put(sArray[i], inc+1);
            }else{
                hm.put(sArray[i], 1);
            }
        }
        int maxCount1 = Integer.MIN_VALUE;
        int maxCount2 = Integer.MIN_VALUE;
        int maxCount3 = Integer.MIN_VALUE;
        String[] result = new String[3];
        for(int j = 0; j < sArray.length; j++){
            int i = hm.get(sArray[j]);
            if(i > maxCount3 && i < maxCount2){
                maxCount3 = i;
                result[2] = sArray[j];
            }
            else if(i > maxCount3 && i < maxCount1){
                maxCount2 = i;
                result[1] = sArray[j];
            }
            else if(i > maxCount1){
                maxCount1 = i;
                result[0] = sArray[j];
            }
        }
        System.out.println(result[2]);
    }
}
