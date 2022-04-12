/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: This class will inherit from List, and function as a Stack data structure.
 * File:        Stack.java
 */

public class Stack<Type> extends List {
    // instance variables - replace the example below with your own
    public Stack() {
        super();
    }

    public void push(Type data) {
        this.Last();
        this.InsertAfter(data);
    }

    public void pop() {
        this.Last();
        this.Remove();
    }

    public Type peek() {
        this.Last();
        return (Type) this.GetValue();
    }
}
