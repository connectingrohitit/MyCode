public class StringBuilders {
    public static void main(String args[]){
        StringBuilder sb = new StringBuilder("Rohit");
        System.out.println(sb);

        //charAt index 0
        System.out.println(sb.charAt(0));

        //set char at index
        sb.setCharAt(4, 'n');
        System.out.println(sb);

        //insert
        sb.insert(3, 'i');
        System.out.println(sb);

        //Append
        sb.append(" Shrivastava");
        System.out.println(sb);
    }
}
