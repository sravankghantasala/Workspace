/**
 * Created by sraone on 10/1/14.
 */
public class Constructors {

//    An empty constructor
    public Constructors (){
//        Just prints
        System.out.println("Hi I am a constructor");
    }

//    A constructor which can accept arguments
    public Constructors (String name) {
        System.out.println("Hi I am a constructor and my new name is " + name);
    }

//    TODO : Have to do Copy Constructor

//    Main method
    public static void main(String[] args) {
//        Creating Constructors object with empty constructor call
        Constructors c1 = new Constructors();
//        Creating Constructors object with argument constructor call
        Constructors c2 = new Constructors("Bub");
    }

}
