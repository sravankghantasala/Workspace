/**
 * Created by sraone on 10/1/14.
 */
public class ClassMethods1 {

    /**
     * A Sample method
     */
    public void method1 () {
        System.out.println("Hi I am method1");
    }

    /**
     * A method which accepts a string argument
     * @param name
     */
    public void method2 (String name) {
        System.out.println("Hi I am method2 and my new name is ... " + name);
    }

    /**
     * A method which accepts a string argument and returns a string
     * @param name
     * @return
     */
    public String method3 (String name) {
        System.out.println("Hi I am method3 and my new name is ... " + name);
        return("and I like it :)");
    }

    public static String method4 (String name) {
        System.out.println("Hi I am a static method with name " + name );
        return ("And I dont need to be called through a class.");
    }

//    Main method
    public static void main(String[] args) {
        ClassMethods1 cm = new ClassMethods1();
//        Calling class methods
        cm.method1();
        cm.method2("Bub");
        System.out.println(cm.method3("Blob"));
//        We can call a static method with out initializing class instance.
        System.out.println(ClassMethods1.method4("Buddy"));
    }
}
