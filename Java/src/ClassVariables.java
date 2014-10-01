/**
 * Created by sraone on 10/1/14.
 */
public class ClassVariables {

    int aNumber;
    String aString;

//    Constructor
    public ClassVariables (int num, String str) {
        this.aNumber = num;
        this.aString = str;
    }

//    Getter and Setter methods
    public String getaString() {
        return aString;
    }

    public void setaString(String aString) {
        this.aString = aString;
    }

    public int getaNumber() {
        return aNumber;
    }

    public void setaNumber(int aNumber) {
        this.aNumber = aNumber;
    }

//    Main Method
    public static void main(String[] args) {
        ClassVariables cv = new ClassVariables(10,"ten");

//        User getter methods to get the values we set from constructor
        System.out.println("the number : " + cv.getaNumber());
        System.out.println("the string : " + cv.getaString());

//        Now use the setter methods to set the values
        cv.setaNumber(100); cv.setaString("hundred");

        System.out.println("the number : " + cv.getaNumber());
        System.out.println("the string : " + cv.getaString());

    }
}
