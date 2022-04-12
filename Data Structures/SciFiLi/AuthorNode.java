/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: This file will contain the definition of a node for a binary tree of books.
 * File:        AuthorNode.java
 */

import java.util.Vector;

public class AuthorNode {
    private String authorName;
    private Vector<String> works;
    private AuthorNode right;
    private AuthorNode left;

    // constructor
    public AuthorNode()
    {
        this.authorName = null;
        this.works = new Vector<String>();
        this.right = null;
        this.left = null;
    }

    public AuthorNode(String s){
        this.authorName = s;
        this.works = new Vector<String>();
        this.right = null;
        this.left = null;
    }

    // accessor and mutator for the data component
    public String getAuthorName()
    {
        return this.authorName;
    }

    public void setAuthorName(String data)
    {
        this.authorName = data;
    }

    // accessor and mutator for the link component
    public AuthorNode getRight()
    {
        return this.right;
    }

    public void setRight(AuthorNode link)
    {
        this.right = link;
    }

    public AuthorNode getLeft()
    {
        return this.left;
    }

    public void setLeft(AuthorNode link)
    {
        this.left = link;
    }

    public Vector<String> getWorks() {return this.works;}

    //Could overload assignment operator, but no.
    public void setWorks(Vector<String> v) { this.works = v;}

    public void addWork(String s) {this.works.add(s);}
}
