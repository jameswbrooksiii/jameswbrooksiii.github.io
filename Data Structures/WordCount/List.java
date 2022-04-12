/* ***************************************************
 * James Brooks
 *
 * List Class - handles any form of data
 *************************************************** */

public class List<Type>
{
    // We don't actually have to set a max size with linked lists
    // But it is a good idea.
    // Just picture an infinite loop adding to the list! :O
    // Yes, you may change this when you do your word count program.
    public static final int MAX_SIZE = 200;

    private Node<Type> head;
    private Node<Type> tail;
    private Node<Type> curr;
    private int num_items;

    // constructor
    // remember that an empty list has a "size" of -1 and its "position" is at -1
    public List()
    {
        
    }

    // copy constructor
    // clones the list l and sets the last element as the current
    // (notice we're not just copying the whole list at once?)
    public List(List<Type> l)
    {
        Node<Type> n = l.head.getLink();

        this.head = this.tail = this.curr = null;
        this.num_items = 0;

        while (n != null)
        {
            this.InsertAfter(n.getData());
            n = n.getLink();
        }
    }

    // navigates to the beginning of the list
    public void First()
    {
        curr.setLink(head.getLink());
    }

    // navigates to the end of the list
    // the end of the list is at the last valid item in the list
    public void Last()
    {
        curr.setLink(tail.getLink());
    }

    // navigates to the specified element (0-index)
    // this should not be possible for an empty list
    // this should not be possible for invalid positions
    public void SetPos(int pos)
    {
        if (head != null && pos < num_items && pos >= 0)
        {
            curr.setLink(head.getLink());
            int currpos = 0;
            while (currpos < pos)
            {
                if (currpos == pos)
                {
                    break;
                }
                else
                {
                    currpos += 1;
                    Next();
                }
            }
        }
    }

    // navigates to the previous element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Prev()
    {
        SetPos(GetPos()-1);
    }

    
    // navigates to the next element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Next()
    {
        if (head != null && curr.getLink().getLink() != null)
        {
            curr.setLink(curr.getLink().getLink());
        }
    }

    // returns the location of the current element (or -1)
    public int GetPos()
    {
        if (num_items < 1)
        {
            return -1;
        }
        else
        {
            Node<Type> posi = head.getLink();
            int pos = 0;
            while (posi != curr.getLink())
            {
                pos += 1;
                posi = posi.getLink();
            }
            return pos;
        }
    }

    // returns the value of the current element (or -1)
    public Type GetValue()
    {
        if (curr == null)
        {
            return null;
        }
        else
        {
            return curr.getLink().getData();
        }
    }

    // returns the size of the list
    // size does not imply capacity
    public int GetSize()
    {
        return num_items;
    }

    // inserts an item before the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertBefore(Type data)
    {
        if (IsFull() == false)
        {
            Node newNode = new Node();
            newNode.setData(data);
            if (head == null)
            {
                head = new Node();
                tail = new Node();
                curr = new Node();
                head.setLink(newNode);
                tail.setLink(newNode);
                curr.setLink(newNode);
                num_items += 1;
            }
            else if (curr.getLink() == head.getLink())
            {
                newNode.setLink(head.getLink());
                curr.setLink(newNode);
                head.setLink(newNode);
                num_items += 1;
            }
            else
            {
                Prev();
                InsertAfter(data);
            }
        }
    }

    // inserts an item after the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertAfter(Type data)
    {
        if (IsFull() == false)
        {
            Node<Type> newNode = new Node();
            newNode.setData(data);
            if (head == null)
            {
                head = new Node();
                tail = new Node();
                curr = new Node();
                head.setLink(newNode);
                tail.setLink(newNode);
                curr.setLink(newNode);
                num_items += 1;
            }
            else if (curr.getLink() == tail.getLink())
            {
                curr.getLink().setLink(newNode);
                curr.setLink(newNode);
                tail.setLink(newNode);
                num_items += 1;
            }
            else
            {
                newNode.setLink(curr.getLink().getLink());
                curr.getLink().setLink(newNode);
                curr.setLink(newNode);
                num_items += 1;
            }
        }
    }

    // removes the current element 
    // this should not be possible for an empty list
    public void Remove()
    {
        if (head != null)
        {
            if (curr.getLink() == head.getLink())
            {
                if (num_items > 0)
                {
                    head.setLink(head.getLink().getLink());
                    First();
                    num_items -= 1;
                }
            }
            else if (curr.getLink() == tail.getLink())
            {
                Prev();
                tail.setLink(curr.getLink());
                curr.getLink().setLink(null);
                num_items -= 1;
            }
            else
            {
                Prev();
                curr.getLink().setLink(curr.getLink().getLink().getLink());
                num_items -= 1;
                Next();
            }
        }
    }

    // replaces the value of the current element with the specified value
    // this should not be possible for an empty list
    public void Replace(Type data)
    {
        if (head != null)
        {
            if (curr.getLink() == head.getLink())
            {
                head.getLink().setData(data);
            }
            if (curr.getLink() == tail.getLink())
            {
                tail.getLink().setData(data);
            }
            else
            {
                curr.getLink().setData(data);
            }
        }
    }

    // returns if the list is empty
    public boolean IsEmpty()
    {
        if (head == null)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    // returns if the list is full
    public boolean IsFull()
    {
        if (GetSize() >= MAX_SIZE)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    // returns if two lists are equal (by value)
    public boolean Equals(List<Type> l)
    {
        Node<Type> A = head.getLink();
        Node<Type> B = l.head.getLink();
        
        int counter = 0;
        if (GetSize() != l.GetSize())
        {
            return false;
        }
        else if (GetSize() == l.GetSize() && counter == GetSize())
        {
            while (counter < GetSize())
            {
                if (A.getData() == B.getData())
                {
                    counter += 1;
                    A = A.getLink();
                    B = B.getLink();
                }
            }
        }
        return true;
    }

    // returns the concatenation of two lists
    // l should not be modified
    // l should be concatenated to the end of *this
    // the returned list should not exceed MAX_SIZE elements
    // the last element of the new list is the current
    public List<Type> Add(List<Type> l)
    {
        List<Type> x = new List<>(this);
        Node<Type> y = l.head.getLink();
        
        while(y != null && x.IsFull() == false)
        {
            x.InsertAfter(y.getData());
            y = y.getLink();
        }
        return x;
    }

    // returns a string representation of the entire list (e.g., 1 2 3 4 5)
    // the string "NULL" should be returned for an empty list
    public String toString()
    {
        if (head == null || num_items <= 0)
        {
            return "NULL";
        }
        else
        {
            String s = "";
            Node<Type> x = head.getLink();
            while (x != null)
            {
                s += x.getData() + " ";
                x = x.getLink();
            }
            return s;
        }
    }
 }
