/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: This file will contain the definition of a node for a binary tree of books.
 * File:        BookNode.java
 */

import java.util.Vector;

public class BookNode {
    private String title;
    private String author;
    private int status;
    private int priority;
    private BookNode right;
    private BookNode left;

    // constructor
    public BookNode()
    {
        this.title = null;
        this.author = null;
        this.status = 1;
        this.priority = -1;
        this.right = null;
        this.left = null;
    }

    public BookNode(String s, String a, int stat, int p){
        this.title = s;
        this.author = a;
        this.status = stat;
        this.priority = p;
        this.right = null;
        this.left = null;
    }

    // accessor and mutator for the data component
    public String getTitle() { return this.title; }

    public void setTitle(String data) { this.title = data; }

    public String getAuthor() { return this.author; }

    public void setAuthor(String a) { this.author = a; }

    public int getStatus() { return this.status; }

    public void setStatus(int num) { this.status = num; }

    public int getPriority() { return this.priority; }

    public void setPriority(int num) { this.priority = num; }

    // accessor and mutator for the link component
    public BookNode getRight() { return this.right; }

    public void setRight(BookNode link) { this.right = link; }

    public BookNode getLeft() { return this.left; }

    public void setLeft(BookNode link) { this.left = link; }
}