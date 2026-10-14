
/**
 * Write a description of class Main here.
 *
 * James Brooks (your name)
 * @version (a version number or a date)
 */
public class Main
{
    public static void main(String args[])
    {
        addNode(5);
        addNode(10);
        int x = 15;
        for (int i=0; i < 6; i++)
        {
            addNode(x);
            x += 5;
        }
        printList();
    }

    public static void addNode(int data) //Assistance acquired from BluePelican textbook
    {
        Node newNode = new Node(data, null);
        if(head == null)
        {
            head = newNode;
        }
        else
        {
            tail.setLink(newNode);
        }
        tail = newNode;
    }
    private static Node head = null;
    private static Node tail = null;
    
    public static void printList()
    {
        Node current = head;
        int nodeNum = -1;
        do
        {
            nodeNum++;
            System.out.println("Node number: " + nodeNum + "\nData: " + current.getData() + "\n");
            current = current.getLink();
        }
        while(current != null);
    }
}
