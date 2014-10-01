/**
 * Created by sraone on 10/1/14.
 */
public class Loops {
    // Main Method
    public static void main(String[] args) {
        System.out.println("Printing 1 to 20 using for loop ... ");
        for (int i=1;i<=20;i++){
            System.out.print(i + " ");
        }

        System.out.println("\n\nPrinting 1 to 20 using while loop ... ");
        int i=1;
        while (i<=20) {
            System.out.print(i + " ");
            i++;
        }

        System.out.println("\n\nPrinting 1 to 20 using do while loop ... ");
//        As i is already defined, we done need to define again.
        i=1;
        do {
            System.out.print(i + " ");
            i++;
        } while (i<=20);

//        for each loop is specially designed for iterating arrays in java and
//                is introduced in java 5.0
        int [] array = {1,2,3,4,5,6,7,8,9};
        System.out.println("\n\nPrinting an array values using for each loop ... ");
        for (int value : array) {
            System.out.print(value + " ");
        }

//        Break a loop upon satisfying a condition using break keyword
        System.out.println("\n\nBreaks a loop upon satisfying a condition ... ");
//        This way is newly introduced in java 6.0
        System.out.println("Please enter a number less than 30 to break the loop there ");
        int n = Integer.parseInt(System.console().readLine());
        for (i=1; i<=30; i++){
            if (i==n) break;
            System.out.print(i + " ");
        }

//        Skip executing rest of the statements in a loop upon satisfying a condition
//                using continue statement
        System.out.println("\n\nSkips printing a number using continue keyword ... ");
        System.out.println("Please enter a number less than 30 to skip the loop there ");
        n = Integer.parseInt(System.console().readLine());
        for (i=1; i<30; i++){
            if (i==n) continue;
            System.out.print(i + " ");
        }
    }
}

