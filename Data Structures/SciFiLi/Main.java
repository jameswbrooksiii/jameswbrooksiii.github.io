/*
 * Author:      Drew Getsinger and James Brooks
 * Date:        11/13/20
 * Project:     SciFiLi
 * Description: Program will use several data structures, searches, and sorts to simulate a bookstore or library's
 *              book handling system.
 * File:        Main.java
 */

//Imports
import java.util.*;
import java.io.*;

public class Main {

    //Globals
    private static final int LIBRARY_SIZE = 100000;

    /** Partition
     *
     * Description: This function will select a pivot pointa and sort all data to one side of the pivot
     *              along with QuikSort.
     *
     * @param b     -   Array of Book Objects
     * @param min   -   Minimum index of partition
     * @param max   -   Maximum index of partition
     * @return      -   Returns the pivot point.
     */
    static int partition(BookNode[] b, int min, int max){
        BookNode pivot = b[max];
        int i = (min-1);

        for(int j = min; j < max; ++j){
            if(b[j].getPriority() < pivot.getPriority()){
                ++i;

                BookNode temp = b[i];
                b[i] = b[j];
                b[j] = temp;
            }
        }

        BookNode temp = b[i+1];
        b[i+1] = b[max];
        b[max] = temp;

        return i+1;
    }

    /** QuikSort
     *
     * Description: This function will act as the driver of the quick sort algorithm to sort the array of
     *              plane objects.
     *
     * @param b     -   Array of Book Objects
     * @param min   -   Minimum index of partition
     * @param max   -   Maximum index of partition
     * @return      -   Void return
     */
    static void quikSort(BookNode[] b, int min, int max){
        if(min < max){
            int part = partition(b, min, max);

            quikSort(b, min, part-1);
            quikSort(b, part+1, max);
        }
    }

    public static void main( String[] args){
        try{
            //Variables
            AuthorTree authorDatabase = new AuthorTree();
            BookTree bookDatabase = new BookTree();
            BookNode[] pList = new BookNode[LIBRARY_SIZE];
            Stack<String> pile = new Stack<String>();
            File bookInput = new File("books.txt");
            File outputFile = new File("SortedBooks.txt");
            Scanner bookParser = new Scanner(bookInput);
            Scanner userInput = new Scanner(System.in);
            String[] splitString = new String[5];
            String userTitle, userAuthor;
            int sTemp, pTemp, userChoice = -1;
            int cnt = 0;

            try {
                FileWriter bookWriter = new FileWriter(outputFile);


                //Read in Books and Populate Trees
                while (bookParser.hasNextLine()) {
                    String data = bookParser.nextLine();
                    splitString = data.split(", ");

                    //Convert Priority and Status
                    sTemp = Integer.parseInt(splitString[2]);
                    pTemp = Integer.parseInt((splitString[3]));

                    //Insert Nodes into Trees
                    authorDatabase.add(splitString[1]);
                    authorDatabase.addToWorks(splitString[1], splitString[0]);
                    bookDatabase.add(splitString[0], splitString[1], sTemp, pTemp);
                    pList[cnt++] = new BookNode(splitString[0], splitString[1], sTemp, pTemp);
                }

                //Display Menu to User and Process Input
                do {
                    System.out.println("\n-----Welcome to James and Drew's Laudable Library-----\n");
                    System.out.println("What would you like to do?\n1)\tSearch Database by Title\n2)\tSearch Database by Author");
                    System.out.println("3)\tCreate List by Title\n4)\tCreate List by Author\n5)\tCheck Book In");
                    System.out.println("6)\tCheck Book Out\n7)\tCreate Priority List\n8)\tQuit Program");
                    System.out.print("Enter Valid Number: ");

                    try {
                        userChoice = userInput.nextInt();
                    } catch (InputMismatchException e) {
                        System.out.println("ERROR: The input was invalid. Stopping program.");
                        System.exit(0);
                    }


                    switch (userChoice) {
                        case 1:
                            System.out.print("Please Enter the Book Title: ");
                            userInput.nextLine();
                            userTitle = userInput.nextLine();
                            BookNode temp = bookDatabase.findBook(userTitle);
                            if (temp != null) {
                                System.out.println("Title:\t\t" + temp.getTitle() + "\nAuthor:\t\t" + temp.getAuthor());
                                System.out.println("Priority:\t" + temp.getPriority());
                                if (temp.getStatus() == 1) {
                                    System.out.println("Status:\t\tChecked In");
                                } else {
                                    System.out.println("Status:\t\tChecked Out");
                                }
                            } else {
                                System.out.println("Work Not Found.");
                            }
                            break;

                        case 2:
                            System.out.print("Please Enter the Author Name: ");
                            userInput.nextLine();
                            userAuthor = userInput.nextLine();
                            AuthorNode temp2 = authorDatabase.findAuthor(userAuthor);
                            if (temp2 != null) {
                                System.out.println("Name:\t\t\t" + temp2.getAuthorName() + "\nList of Works:\t"
                                        + temp2.getWorks().toString());
                            } else {
                                System.out.println("Author Not Found.");
                            }
                            break;

                        case 3:
                            System.out.println("These Are the Works by Title:");
                            bookDatabase.printInOrder();
                            break;

                        case 4:
                            System.out.println("These Are the Authors We Keep:");
                            authorDatabase.printInOrder();
                            break;

                        case 5:
                            System.out.print("Please Enter the Book Title: ");
                            userInput.nextLine();
                            userTitle = userInput.nextLine();
                            pile.push(userTitle);
                            break;

                        case 6:
                            System.out.print("Please Enter the Book Title: ");
                            userInput.nextLine();
                            userTitle = userInput.nextLine();
                            bookDatabase.checkOut(userTitle);
                            break;

                        case 7:
                            quikSort(pList, 0, cnt - 1);
                            System.out.println("Displaying Priority List of Books:");
                            System.out.println("Priority\tTitle");
                            for (int i = 0; i < cnt; ++i) {
                                System.out.println(pList[i].getPriority() + "\t\t\t" + pList[i].getTitle());
                            }
                            break;

                        case 8:
                            while (!pile.IsEmpty()) {
                                System.out.println("Accounting for Books in Check-In Pile...");
                                System.out.println(pile.peek() + "...");
                                bookDatabase.checkIn(pile.peek());
                                pile.pop();
                            }
                            BookNode tempB;
                            boolean swapped;
                            for (int i = 0; i < cnt - 1; i++)
                            {
                                swapped = false;
                                for (int j = 0; j < cnt - i - 1; j++)
                                {
                                    if (pList[j].getTitle().toLowerCase().compareTo(pList[j + 1].getTitle().toLowerCase()) > 0) {
                                        tempB = pList[j];
                                        pList[j] = pList[j + 1];
                                        pList[j + 1] = tempB;
                                        swapped = true;
                                    }
                                }
                                if (!swapped)
                                    break;
                            }
                            bookWriter.write("Sorted List of Statuses and Titles:\n");
                            for(int i = 0; i < cnt; ++i){
                                if (pList[i].getStatus() == 1) {
                                    bookWriter.write("Checked In\t");
                                } else {
                                    bookWriter.write("Checked Out\t");
                                }
                                bookWriter.write(pList[i].getTitle() + "\n");
                            }
                            userChoice = -1;
                            break;
                    }

                } while (userChoice >= 0 && userChoice <= 8);
                bookWriter.close();
            }catch(IOException e){
                System.out.println("An error occurred.");
                e.printStackTrace();
            }
            bookParser.close();
        } catch (FileNotFoundException e){
            System.out.println("ERROR: Book file was not detected at specified path.");
            e.printStackTrace();
            System.exit(0);
        }
    }
}
