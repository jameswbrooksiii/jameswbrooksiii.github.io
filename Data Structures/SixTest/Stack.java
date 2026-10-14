
/**
 * Write a description of class Stack here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Stack<Type> extends List
{
    // instance variables - replace the example below with your own
    public Stack()
    {
        super();
    }

    public void push(Type data)
    {
        this.Last();
        InsertAfter(data);
    }
    
    public void pop()
    {
        this.Last();
        this.Remove();
    }
    
    public Type peek()
    {
        this.Last();
        return (Type)this.GetValue();
    }
}
