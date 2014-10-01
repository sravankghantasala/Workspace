/**
 * Created by sraone on 10/1/14.
 */
public class Conditions {
    // Main Method
    public static void main(String[] args) {
//        simple if conditions
        System.out.println("Enter your favorite movie ... ");
        String n=System.console().readLine();
        if ( n.equals ("ip man")) System.out.println("Mine too ... :)");

//        if else
        System.out.println("Enter your favorite comedy series ... ");
        n = System.console().readLine();
        if ( n.equals( "2 n half men")) System.out.println("Mine too ... :)");
        else System.out.println("Oh ok! Mine is 2 n half men");

//        if elseif
        System.out.println("Enter your favorite taste ... ");
        n = System.console().readLine();
        if (n.equals("spice")) System.out.println("Mine too ... :)");
        else if (n.equals("sour")) System.out.println("I hate it buddy ... :(");
        else System.out.println("Ahh ok!. Mine is Spice ");

//        switch case implementation
        System.out.println("Enter your favorite super hero ... ");
        n = System.console().readLine().toString();
        switch (n.toLowerCase()){
            case "batman":
                System.out.println("Awesome! we are like brother buddy ... :)");
                break;
            case "hulk":
                System.out.println("Aww! I like him too ... :)");
                break;
            case "superman":
                System.out.println("You serious?! No kidding right");
                break;
            default:
                System.out.println("Did you ever watched a super hero ?");
                break;
        }
    }
}
