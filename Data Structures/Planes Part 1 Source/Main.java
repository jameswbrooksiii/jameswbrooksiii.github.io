
/**
 * The Main part of the Planes Part 1 Program. Displays a menu for the user. User may list a bubble sorted Array of planes, binary search for a specific
 * plane number, or exit the program.
 *
 * James Brooks
 * 9/19/2020 (Late Submission!)
 */

import java.io.*;
import java.util.*;
public class Main
{
    public static void main(String[] args) throws Exception
    {
        Plane PlaneArray[] = new Plane[29]; // Creates initial array
        PlaneArray = FileReader(); // Starts the FileReader, which feeds into the array sorter as well.
        Scanner MenuScanner = new Scanner(System.in); // Makes a Scanner for user input.
        displayMenu(); // Prints the menu.
        boolean running = true; // While the menu is still running...
        while(running ==true)
        {
            int menuInput = MenuScanner.nextInt(); // Detect user input.
            switch(menuInput)
            {
                default: // The default response. Sent if 0, 1, or 2 is not entered initially.
                    System.out.println("-----------------------------");
                    System.out.println("I don't understand. Please try one of the listed options.");
                    System.out.println("-----------------------------");
                    displayMenu();
                    break;
                case 0: // Prints the sorted list of Planes.
                    System.out.println("-----------------------------");
                    printArray(PlaneArray);
                    System.out.println("-----------------------------");
                    displayMenu();
                    break;
                case 1: // Searches for a Plane using binary search.
                    System.out.println("Enter a Plane ID to search for.");
                    Plane ID = searchPlane(PlaneArray, MenuScanner.nextInt());
                    System.out.println("-----------------------------");
                    if(ID == null) // If a plane is not found, say Plane not here.
                    {
                        System.out.println("Plane not here.");
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                    else // If a plane is found, print it's information.
                    {
                        System.out.println(ID);
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                        
                case 2: // Exit if the user wishes to exit.
                    System.out.println("-----------------------------");
                    System.out.println("Exiting.");
                    System.out.println("-----------------------------");
                    running = false;
                    break;
            }
        }
        MenuScanner.close(); // Close scanner.
    }
    public static void displayMenu()
    {
        System.out.println("Please enter one of the following.\n" + "0: List Planes\n" + "1: Find Plane\n" + "2: Exit"); // Prints the menu.
    }
    public static Plane[] FileReader() throws IOException
    {
        Scanner sf = new Scanner(new File("planes.txt")); // Collects and reads the planes.txt file. This was included in the zip, so the directory should work.
        String spArray[];
        String x;
        Plane FirstArray[] = new Plane[29];
        int maxIndx = -1;
        String text[] = new String[1000];
        
        while(sf.hasNext())
        {
            maxIndx++;
            text[maxIndx] = sf.nextLine();
        }
        sf.close(); // Closes the text file scanner.
        
        for(int j=1; j <= 28; j++) // By starting at line 1 instead of 0, the string skips the header.
        {
            x = text[j];
            spArray = x.split(",\\s"); // Splits the string, removing commas and whitespace and inserting the rest into an array.
            int PlaneNum = Integer.parseInt(spArray[0]);
            String Destination = spArray[1];
            int DayOfTravel = Integer.parseInt(spArray[2]);
            String Meal = spArray[3];
            int Rows = Integer.parseInt(spArray[4]);
            int NumPerRows = Integer.parseInt(spArray[5]);
            Plane pl = new Plane(PlaneNum, Destination, DayOfTravel, Meal, Rows, NumPerRows);
            FirstArray[j-1] = pl;
        }
        return SortArray(FirstArray); // Returns the unsorted array of planes to the array sorter.
    }
    public static Plane[] SortArray(Plane SortedArray[])
    {
        int n = SortedArray.length;
        for(int i=0; i < n-1; i++)
        {
            for(int j=0; j<n-i-1;j++)
            {
                if(j<27) // Sorts the array using bubble sort.
                {
                    int One = SortedArray[j].getPlaneNum();
                    int x = j+1;
                    int Two = SortedArray[x].getPlaneNum();
                    if(One > Two)
                    {
                        Plane temp = SortedArray[j];
                        SortedArray[j] = SortedArray[j+1];
                        SortedArray[j+1] = temp;
                    }
                }
            }
        }
        return SortedArray; // Returns the Sorted Array to be used in the main function, for the list and search.
    }
    public static void printArray(Plane[] SortedArray)
    {
        for(int i=0; i < 28; i++)
        {
            System.out.println(SortedArray[i].toString()); // Converts an Array to String.
        }
    }
    public static Plane searchPlane(Plane pl[], int ID) // Boolean search. Shows comparisons in realtime.
    {
        int bot = 0;
        int top = pl.length+1;
        boolean searching = true;
        System.out.println("-----------------------------");
        System.out.println("Running comparisons...");
        do
        {
            int mid = (bot + top)/2;
            if (bot == 28|top == -1) // Breaks and returns null if plane is not found.
            {
                System.out.println("Plane NOT found.");
                searching = false;
                break;
            }
            else if(ID == pl[mid].getPlaneNum()) // Returns the current middle as the correct plane if it is found.
            {
                System.out.println("Plane found.");
                return pl[mid];
            }
            else if (ID > pl[mid].getPlaneNum()) // If the Plane you're looking for is higher, raise the bottom and search again.
            {
                System.out.println("COMPARE: " + ID + " TO " + pl[mid].getPlaneNum());
                bot = mid+1;
                System.out.println("BOTTOM: " + bot);
            }
            else if (ID < pl[mid].getPlaneNum()) // If the Plane you're looking for is lower, lower the top and search again.
            {
                System.out.println("COMPARE: " + ID + " TO " + pl[mid].getPlaneNum());
                top = mid-1;
                System.out.println("TOP: " + top);
            }
        }
        while(searching == true);
        return null;
    }    
}
