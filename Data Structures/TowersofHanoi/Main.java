
/**
 * Write a description of class Main here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Main
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class Main
     */
    public static void main(String[] args)
    {
        // initialise instance variables
        Hanoi(5, 1, 3, 2);
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static void Hanoi(int n, int from, int to, int spare)
    {
        if (n == 1) 
        { 
            System.out.println(from + " --> " + to);
            return;
        }
        Hanoi(n-1, from, spare, to);
        Hanoi(1, from, to, spare);
        Hanoi(n-1, spare, to, from);
    }
}
