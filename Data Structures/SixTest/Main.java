
/**
 * Write a description of class Main here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception
    {
        // Number 1, reading the file and storing the books, will happen here.
        Scanner scanner = new Scanner(System.in);
        displayMenu();
        boolean running = true;
        // Currently I've just got it set up to be a lot like the Planes project we did,
        // where it displays a menu and then takes a user input for a switch case to run
        // a function.
        // Case 4 has the returning the stack of books thing.
        while (running == true)
        {
            int menuInput = scanner.nextInt();
            switch(menuInput)
            {
                default:
                    System.out.println("\nI don't understand. Please try one of the listed options.\n");
                    displayMenu();
                    break;
                    
                case 1:
                    System.out.println("\nThis is where the program would search by title or author.\n");
                    displayMenu();
                    break;
                    
                case 2:
                    System.out.println("\nThis is where the program will list books by title or author.\n");
                    displayMenu();
                    break;
                
                case 3:
                    System.out.println("\nThis is where the program will be able to check in or check out books.\n");
                    displayMenu();
                    break;
                
                case 4: // This is the one that I've written
                    returnbooks();
                    displayMenu();
                    break;
                
                case 5:
                    System.out.println("\nThis is where the program prints out a list organized by priority.\n");
                    displayMenu();
                    break;
                
                case 6:
                    System.out.println("\nExiting.\n");
                    running = false;
                    break;
            }
        }
        scanner.close();
    }
    public static void displayMenu()
    {
        System.out.println("Please enter one of the following.\n" + "1: Search by Title or Author\n" + "2: List Books by Title or Author\n" + "3: Check In or Check Out Books\n" + "4: Return Books (USE THIS ONE)\n" + "5: Display Emergency Priority List\n" + "6: Exit\n");
    }
    public static void returnbooks()
    {
        Stack<String> stack = new Stack<>(); // Initializes stack. Stack is repurposed from the Teacher's Helper code.
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nPlease enter one of the following.\n" + "1: Add a Book to the Pile\n" + "2: Return all books on the Pile\n");
        boolean returning = true;
        // Another switch case, just figured that it'd be easier to do and read.
        while (returning == true)
        {
            int menuInput = scanner.nextInt();
            switch(menuInput)
            {
                default:
                    System.out.println("\nI don't understand. Please try one of the listed options.\n");
                    System.out.println("\nPlease enter one of the following.\n" + "1: Add a Book to the Pile\n" + "2: Return all books on the Pile\n");
                    break;
                    
                case 1:
                    System.out.println("\nPlease enter the name of the book being added to the pile.\n");
                    String title = scanner.next();
                    // For this part, search for the book using search function made for
                    // requirement 2, with the title string made as the argument.
                    // If the title is not found, do this
                    // if(BookTree.SearchTitle(title) == null)
                    // {
                    //      System.out.println("\n Book not found, or Title was typed incorrectly.\n");
                    //      System.out.println("\nPlease enter one of the following.\n" + "1: Add a Book to the Pile\n" + "2: Return all books on the Pile\n");
                    //      break;
                    // }
                    // If the book is found, check if it's already returned.
                    // If it is, then break.
                    // if(Book.getCheckStatus == 1)
                    // {
                    //      System.out.println("\nThat Book is already checked in!\n");
                    //      System.out.println("\nPlease enter one of the following.\n" + "1: Add a Book to the Pile\n" + "2: Return all books on the Pile\n");
                    //      break;
                    // }
                    // Else, the book is pushed onto the stack.
                    // else
                    // {
                    // stack.push(book);
                    stack.push(title);
                    System.out.println("\nPlease enter one of the following.\n" + "1: Add a Book to the Pile\n" + "2: Return all books on the Pile\n");
                    break;
                    
                case 2:
                    while (stack.IsEmpty() != true)
                    {
                        if(stack.peek() == null)
                        {
                            break;
                        }
                        else
                        {
                            // This is the part where a function would be called, that adds
                            // each book from the stack to the list/tree. For now, the stack
                            // just prints the book title, then pops.
                            // stack.peek().setCheckStatus(1);
                            System.out.println(stack.peek());
                            stack.pop();
                        }
                    }
                    System.out.println("\nPile of books returned.\n");
                    returning = false;
                    break;
            }
        }
        scanner.close();
    }
}
