
/**
 * Write a description of class Node here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
class Node
{
    // instance variables - replace the example below with your own
    private int data;
    private Node link;

    public Node()
    {
        // initialise instance variables
        this.data = 0;
        this.link = null;
    }
    public Node(int data)
    {
        this.data = data;
        this.link = link;
    }

    public int getData()
    {
        // put your code here
        return this.data;
    }
    public void setData(int data)
    {
        this.data = data;
    }
    
    public Node getLink()
    {
        return this.link;
    }
    public void setLink(Node link)
    {
        this.link = link;
    }
}
