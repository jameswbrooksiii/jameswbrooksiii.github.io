/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: Program will use several data structures, searches, and sorts to simulate a bookstore or library's
 *              book handling system.
 * File:        Main.java
 */

public class List<Type>
{
    // We don't actually have to set a max size with linked lists
    // But it is a good idea.
    // Just picture an infinite loop adding to the list! :O
    // Yes, you may change this when you do your word count program.
    public static final int MAX_SIZE = 50;

    private Node<Type> head;
    private Node<Type> tail;
    private Node<Type> curr;
    private int num_items;

    // constructor
    // remember that an empty list has a "size" of -1 and its "position" is at -1
    public List()
    {
        this.head = this.tail = this.curr = null;
        this.num_items = 0;
    }

    // copy constructor
    // clones the list l and sets the last element as the current
    // (notice we're not just copying the whole list at once?)
    public List(List<Type> l)
    {
        Node<Type> n = l.head;

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
        this.curr = this.head;
    }

    // navigates to the end of the list
    // the end of the list is at the last valid item in the list
    public void Last()
    {
        this.curr = this.tail;
    }

    // navigates to the specified element (0-index)
    // this should not be possible for an empty list
    // this should not be possible for invalid positions
    public void SetPos(int pos)
    {
        if(this.head != null && pos >= 0 && pos < this.num_items){
            First();
            for(int i = 0; i < pos; ++i){
                this.curr = this.curr.getLink();
            }
        } else {
            //System.out.println("ERROR: Invalid index parameter to set current pointer.");
        }
    }

    // navigates to the previous element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Prev()
    {
        Node<Type> temp = this.head;

        if(this.head != null){
            if(this.curr != this.head){
                while(temp.getLink() != this.curr){
                    temp = temp.getLink();
                }
                this.curr = temp;
            }
        } else {
            System.out.println("ERROR: Cannot navigate on an empty list.");
        }
    }


    // navigates to the next element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Next()
    {
        if(this.head != null){
            if(this.curr != this.tail){
                this.curr = this.curr.getLink();
            }
        } else {
            System.out.println("ERROR: Cannot navigate on an empty list.");
        }
    }

    // returns the location of the current element (or -1)
    public int GetPos()
    {
        int ndx = 0;
        Node<Type> temp = this.head;

        if(this.curr == null){
            return -1;
        }

        if(this.head != null){
            while(temp != this.curr){
                temp = temp.getLink();
                ++ndx;
            }
        }
        return ndx;
    }

    // returns the value of the current element (or -1)
    public Type GetValue()
    {
        if(this.curr != null){
            return this.curr.getData();
        } else {
            System.out.println("ERROR: Cannot retrieve value from empty list.");
        }
        return null;
    }

    // returns the size of the list
    // size does not imply capacity
    public int GetSize()
    {
        return this.num_items;
    }

    // inserts an item before the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertBefore(Type data)
    {
        if(this.head != null && this.num_items < MAX_SIZE){
            Node<Type> tempI = new Node<Type>();
            Node<Type> temp = this.head;
            tempI.setData(data);

            if(this.curr != this.head){
                temp = this.head;
                while(temp.getLink() != this.curr){
                    temp = temp.getLink();
                }
                temp.setLink(tempI);
                tempI.setLink(this.curr);
                this.curr = tempI;
            } else {
                tempI.setLink(this.head);
                this.head = tempI;
                this.curr = tempI;
            }
            ++this.num_items;
        } else {
            if(this.num_items == 0){
                Node<Type> tempI = new Node<Type>();
                tempI.setData(data);
                this.head = this.curr = this.tail = tempI;
                ++this.num_items;
            } else {
                //System.out.println("ERROR: List is full");
            }
        }
    }

    // inserts an item after the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertAfter(Type data)
    {
        if(this.head != null && this.num_items < MAX_SIZE){
            Node<Type> tempI = new Node<Type>();
            tempI.setData(data);

            if(this.curr != this.tail){
                tempI.setLink(this.curr.getLink());
                this.curr.setLink(tempI);
                this.curr = tempI;
            } else {
                tempI.setLink(this.curr.getLink());
                this.curr.setLink(tempI);
                this.curr = tempI;
                this.tail = tempI;
            }
            ++this.num_items;
        } else {
            if(this.num_items == 0){
                Node<Type> tempI = new Node<Type>();
                tempI.setData(data);
                this.head = this.curr = this.tail = tempI;
                ++this.num_items;
            } else {
                //System.out.println("ERROR: List is full");
            }
        }
    }

    // removes the current element 
    // this should not be possible for an empty list
    public void Remove()
    {
        if(this.head != null){
            Node<Type> temp = this.head;

            if(this.curr != this.head){
                while(temp.getLink() != this.curr){
                    temp = temp.getLink();
                }
                temp.setLink(this.curr.getLink());
                if(this.curr != this.tail)
                    this.curr = this.curr.getLink();
                else {
                    this.tail = temp;
                    this.curr = temp;
                }
                --this.num_items;
            } else if(this.head != this.tail){
                this.head = this.head.getLink();
                this.curr.setLink(null);
                this.curr = this.head;
                --this.num_items;
            } else {
                this.curr = null;
                this.tail = null;
                this.head = null;
                --this.num_items;
            }
        } else {
            //System.out.println("ERROR: Cannot remove on an empty list.");
        }
    }

    // replaces the value of the current element with the specified value
    // this should not be possible for an empty list
    public void Replace(Type data)
    {
        if(this.head != null){
            this.curr.setData(data);
        } else {
            System.out.println("ERROR: Cannot replace on empty list.");
        }
    }

    // returns if the list is empty
    public boolean IsEmpty()
    {
        if(this.head == null)
            return true;
        else
            return false;
    }

    // returns if the list is full
    public boolean IsFull()
    {
        if(this.num_items == MAX_SIZE)
            return true;
        else
            return false;
    }

    // returns if two lists are equal (by value)
    public boolean Equals(List<Type> l)
    {
        Node<Type> temp1 = this.head;
        Node<Type> temp2 = l.head;

        if(temp1 == null && temp2 == null)
            return true;
        else if(temp1 == null)
            return false;
        else if(temp2 == null)
            return false;

        while(temp1 != null && temp2 != null){
            if(temp1.getData() != temp2.getData()){
                return false;
            }
            temp1 = temp1.getLink();
            temp2 = temp2.getLink();
        }
        if(temp1 == null && temp2 == null)
            return true;
        else
            return false;
    }

    // returns the concatenation of two lists
    // l should not be modified
    // l should be concatenated to the end of *this
    // the returned list should not exceed MAX_SIZE elements
    // the last element of the new list is the current
    public List<Type> Add(List<Type> l)
    {
        if(this.head == null){
            List<Type> temp = new List<Type>(l);
            return temp;
        }

        if(this.num_items + l.num_items <= MAX_SIZE){
            Node<Type> tempN = this.tail;

            this.tail.setLink(l.head);
            this.tail = l.tail;

            List<Type> temp = new List<Type>(this);

            this.tail = tempN;
            this.tail.setLink(null);

            return temp;
        }
        return null;
    }

    // returns a string representation of the entire list (e.g., 1 2 3 4 5)
    // the string "NULL" should be returned for an empty list
    public String toString()
    {
        Node<Type> temp = this.head;
        String listS = "";
        if(this.head != null){
            while(temp != null){
                listS = listS + temp.getData() + " ";
                temp = temp.getLink();
            }
            return listS;
        } else {
            return "NULL";
        }
    }
}