
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
        insertNode(10, 12);
        deleteNode(5);
        Node current = head;
        do
        {
            current.setData(current.getData()*current.getData());
            current = current.getLink();
        }
        while(current != null);
        printList();
    }

    public static void addNode(int data) //Assistance acquired from BluePelican textbook
    {
        Node newNode = new Node(data);
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
    
    public static void insertNode(int prevData, int newData)
    {
        Node current = head;
        Node newNode = new Node(newData);
        int nodeNum = -1;
        do
        {
            nodeNum++;
            if(current.getData() == prevData)
            {
                newNode.setLink(current.getLink());
                current.setLink(newNode);
                break;
            }
            else
            {
                current = current.getLink();
            }
        }
        while(current != null);
    }
    
    public static void deleteNode(int data)
    {
        Node current = head;
        int nodeNum = -1;
        do
        {
            nodeNum++;
            //Node next = current.getLink();
            if(head.getData() == data)
            {
                current.setData(0);   
                head = (current.getLink());
                current.setLink(null);
                break;
            }
            else if((current.getLink()).getData() == data)
            {
                current.setLink(current.getLink().getLink());
                current.getLink().setData(0);
                current.getLink().setLink(null);
                break;
            }
            else
            {
                current = current.getLink();
            }
        }
        while(current != null);
    }
                
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

