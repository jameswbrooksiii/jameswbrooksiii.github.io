/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: This file will contain the definition of a binary tree structure for the library.
 * File:        BookTree.java
 */

import java.util.Vector;

public class BookTree{

    //Member Variables
    private BookNode root;
    private int num_items;


    //Member Functions
    public BookTree(){
        this.root = null;
        num_items = 0;
    }

    public BookTree(BookTree t){
        this.root = null;
        //MAYBE
    }

    public BookNode getRoot(){return this.root;}

    public int getNum_items(){return this.num_items;}

    private boolean containsNodeRecursive(BookNode current, String t) {
        if (current == null) {
            return false;
        }
        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) == 0) {
            return true;
        }
        return t.toLowerCase().compareTo(current.getTitle().toLowerCase()) < 0
                ? this.containsNodeRecursive(current.getLeft(), t)
                : this.containsNodeRecursive(current.getRight(), t);
    }

    public boolean containsNode(String t) {
        return this.containsNodeRecursive(this.root, t);
    }

    public BookNode findBookHelper(BookNode current, String t){
        if (current == null) {
            return null;
        }

        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) == 0) {
            return current;
        }

        return t.toLowerCase().compareTo(current.getTitle().toLowerCase()) < 0
                ? this.findBookHelper(current.getLeft(), t)
                : this.findBookHelper(current.getRight(), t);
    }

    public BookNode findBook(String t) {
        return this.findBookHelper(this.root, t);
    }

    public void checkInHelper(BookNode current, String t){
        if (current == null) {
            System.out.println("Error: Typo in Title.");
            return;
        }

        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) == 0) {
            if(current.getStatus() != 1)
                current.setStatus(1);
            else
                System.out.println("Book Already Checked-In");
            return;
        }

        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) < 0)
            this.checkInHelper(current.getLeft(), t);
        else
            this.checkInHelper(current.getRight(), t);
    }

    public void checkIn(String t){
        this.checkInHelper(this.root, t);
    }

    public void checkOutHelper(BookNode current, String t){
        if (current == null) {
            System.out.println("Error: Typo in Title.");
            return;
        }

        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) == 0) {
            if(current.getStatus() != 0)
                current.setStatus(0);
            else
                System.out.println("Book Already Checked-In");
            return;
        }

        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) < 0)
            this.checkOutHelper(current.getLeft(), t);
        else
            this.checkOutHelper(current.getRight(), t);
    }

    public void checkOut(String t){
        this.checkOutHelper(this.root, t);
    }

    public BookNode insert(BookNode current, String t, String a, int stat, int priority) {
        if(current == null){
            return new BookNode(t, a, stat, priority);
        }

        if(t.toLowerCase().compareTo(current.getTitle().toLowerCase()) < 0){
            current.setLeft(this.insert(current.getLeft(), t, a, stat, priority));
        } else if(t.toLowerCase().compareTo(current.getTitle().toLowerCase()) > 0) {
            current.setRight(this.insert(current.getRight(), t, a, stat, priority));
        } else {
            return current;
        }
        return current;
    }

    public void add(String t,String a, int stat, int priority){
        this.root = this.insert(this.root, t, a, stat, priority);
        ++this.num_items;
    }

    private BookNode removeRecursive(BookNode current, String t) {
        if (current == null) {
            return null;
        }

        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) == 0) {
            if (current.getLeft() == null && current.getRight() == null) {                              //Case 1
                return null;
            }

            if (current.getRight() == null) {                                                           //Case 2
                return current.getLeft();
            }

            if (current.getLeft() == null) {
                return current.getRight();
            }

            String smallestValue = this.findSmallestValue(current.getRight());                               //Case 3
            current.setTitle(smallestValue);
            current.setRight(this.removeRecursive(current.getRight(), smallestValue));
            return current;
        }
        if (t.toLowerCase().compareTo(current.getTitle().toLowerCase()) < 0) {
            current.setLeft(this.removeRecursive(current.getLeft(), t));
            return current;
        }
        current.setRight(this.removeRecursive(current.getRight(), t));
        return current;
    }

    private String findSmallestValue(BookNode r) {
        return r.getLeft() == null ? r.getTitle() : this.findSmallestValue(this.root.getLeft());
    }

    public void remove(String t) {
        this.root = this.removeRecursive(this.root, t);
        --this.num_items;
    }

    public void traverseInOrder(BookNode node) {
        if (node != null) {
            this.traverseInOrder(node.getLeft());
            System.out.println(node.getTitle());
            this.traverseInOrder(node.getRight());
        }
    }

    public void printInOrder(){
        this.traverseInOrder(this.root);
    }

    //TESTING METHODS
    private BookTree createBinaryTree() {
        BookTree bt = new BookTree();

        bt.add("Cat", "The Hat", 1, 0);
        bt.add("Wat", "The Hat", 1, 7);
        bt.add("Kat", "The Hat", 1, 3);
        bt.add("Sat", "The Hat", 1, 8);
        bt.add("Lat", "The Hat", 1, 2);
        bt.add("Rat", "The Hat", 1, 1);
        bt.add("Bat", "The Hat", 0, 100);
        bt.add("Mat", "The Hat", 1, 22);

        return bt;
    }

    public void givenABinaryTree_WhenAddingElements_ThenTreeContainsThoseElements() {
        BookTree bt = createBinaryTree();

        if(!bt.containsNode("Rat"))
            System.exit(0);

        if(!bt.containsNode("Cat"))
            System.exit(0);

        if(!bt.containsNode("Lat"))
            System.exit(0);

        if(!bt.containsNode("Mat"))
            System.exit(0);

        if(bt.containsNode("Drew"))
            System.exit(0);

        System.out.println("LETS GOOOO");
    }

    public void givenABinaryTree_WhenDeletingElements_ThenTreeDoesNotContainThoseElements() {
        BookTree bt = createBinaryTree();

        if(!bt.containsNode("Cat"))
            System.exit(0);

        bt.remove("Cat");

        if(bt.containsNode("Cat"))
            System.exit(0);

        if(!bt.containsNode("Mat"))
            System.exit(0);

        bt.remove("Mat");

        if(bt.containsNode("Mat"))
            System.exit(0);

        System.out.println("WE'RE OUT HERE");
    }
}