public class SimpleClass {
    // Instance variable
    private String message;

    // Constructor
    public SimpleClass(String message) {
        this.message = message;
    }

    // Getter for the message
    public String getMessage() {
        return message;
    }

    // Setter for the message
    public void setMessage(String message) {
        this.message = message;
    }

    // Main method for testing
    public static void main(String[] args) {
        SimpleClass obj = new SimpleClass("Hello, World!");
        System.out.println(obj.getMessage());
    }
}
