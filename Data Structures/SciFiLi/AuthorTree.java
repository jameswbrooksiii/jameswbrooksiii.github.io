/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: This file will contain the definition of a binary tree structure for the library.
 * File:        AuthorTree.java
 */

import java.util.Vector;

public class AuthorTree {

    //Member Variables
    private AuthorNode root;
    private int num_items;


    //Member Functions
    public AuthorTree(){
        this.root = null;
        num_items = 0;
    }

    public AuthorTree(AuthorTree t){
        this.root = null;
        //MAYBE
    }

    public AuthorNode getRoot(){return this.root;}

    public int getNum_items(){return this.num_items;}

    private boolean containsNodeRecursive(AuthorNode current, String name) {
        if (current == null) {
            return false;
        }
        if (name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) == 0) {
            return true;
        }
        return name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) < 0
                ? this.containsNodeRecursive(current.getLeft(), name)
                : this.containsNodeRecursive(current.getRight(), name);
    }

    public boolean containsNode(String name) {
        return this.containsNodeRecursive(this.root, name);
    }

    public AuthorNode findAuthorHelper(AuthorNode current, String name){
        if (current == null) {
            return null;
        }

        if (name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) == 0) {
            return current;
        }

        return name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) < 0
                ? this.findAuthorHelper(current.getLeft(), name)
                : this.findAuthorHelper(current.getRight(), name);
    }

    public AuthorNode findAuthor(String name) {
        return this.findAuthorHelper(this.root, name);
    }

    public void addToWorksHelper(AuthorNode current, String name, String s){
        if (current == null) {
            return;
        }

        if (name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) == 0) {
            current.addWork(s);
        }

        if (name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) < 0)
            this.addToWorksHelper(current.getLeft(), name, s);
        else
            this.addToWorksHelper(current.getRight(), name, s);
    }

    public void addToWorks(String name, String s){
        this.addToWorksHelper(this.root, name, s);
    }

    public AuthorNode insert(AuthorNode current, String name) {
        if(current == null){
            return new AuthorNode(name);
        }

        if(name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) < 0){
            current.setLeft(insert(current.getLeft(), name));
        } else if(name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) > 0) {
            current.setRight(insert(current.getRight(), name));
        } else {
            return current;
        }
        return current;
    }

    public void add(String name){
        this.root = this.insert(this.root, name);
        ++this.num_items;
    }

    private AuthorNode removeRecursive(AuthorNode current, String name) {
        if (current == null) {
            return null;
        }

        if (name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) == 0) {
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
            current.setAuthorName(smallestValue);
            current.setRight(this.removeRecursive(current.getRight(), smallestValue));
            return current;
        }
        if (name.toLowerCase().compareTo(current.getAuthorName().toLowerCase()) < 0) {
            current.setLeft(this.removeRecursive(current.getLeft(), name));
            return current;
        }
        current.setRight(this.removeRecursive(current.getRight(), name));
        return current;
    }

    private String findSmallestValue(AuthorNode r) {
        return r.getLeft() == null ? r.getAuthorName() : this.findSmallestValue(this.root.getLeft());
    }

    public void remove(String name) {
        this.root = this.removeRecursive(this.root, name);
        --this.num_items;
    }

    public void traverseInOrder(AuthorNode node) {
        if (node != null) {
            this.traverseInOrder(node.getLeft());
            System.out.println(node.getAuthorName());
            this.traverseInOrder(node.getRight());
        }
    }

    public void printInOrder(){
        this.traverseInOrder(this.root);
    }

    //TESTING METHODS
    private AuthorTree createBinaryTree() {
        AuthorTree bt = new AuthorTree();

        bt.add("Cat");
        bt.add("Dog");
        bt.add("Rat");
        bt.add("Bat");
        bt.add("Sat");
        bt.add("Lat");
        bt.add("Mat");

        return bt;
    }

    public void givenABinaryTree_WhenAddingElements_ThenTreeContainsThoseElements() {
        AuthorTree bt = createBinaryTree();

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
        AuthorTree bt = createBinaryTree();

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
