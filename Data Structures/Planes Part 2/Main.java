
/**
 * The Main part of the Planes Part 2 Program. Displays a menu for the user. User may add passengers, print a sorted list of planes, list passengers on a specific plane, display food count on that
 * plane, search for a specific passenger on a specific plane, search for a specific plane, or exit.
 *
 * James Brooks
 * 9/25/2020
 */

import java.io.*;
import java.util.*;
public class Main
{
    public static void main(String[] args) throws Exception
    {
        Plane PlaneArray[] = new Plane[29]; // Creates initial array
        PlaneArray = PlaneFileReader(); // Starts the FileReader, which feeds into the array sorter as well.
        makeBookings(PlaneArray); // Creates Bookings Array
        analyzeAndSetTakenSeats(PlaneArray); // Sets the value for the seats taken
        Scanner MenuScanner = new Scanner(System.in); // Makes a Scanner for user input.
        displayMenu(); // Prints the menu.
        boolean running = true; // While the menu is still running...
        while(running ==true)
        {
            int menuInput = MenuScanner.nextInt(); // Detect user input.
            switch(menuInput)
            {
                default: // The default response. Sent if any correct number is not entered initially.
                    System.out.println("-----------------------------");
                    System.out.println("I don't understand. Please try one of the listed options.");
                    System.out.println("-----------------------------");
                    displayMenu();
                    break;
                    
                case 0: // The Add Passenger function
                    System.out.println("Enter a Plane ID to add a passenger to.");
                    Plane passPlaneID = searchPlane(PlaneArray, MenuScanner.nextInt());
                    System.out.println("-----------------------------");
                    System.out.println("Enter a passenger name to add.");
                    String passName = MenuScanner.next();
                    System.out.println("Enter the passenger's food preference (chicken, pasta, or special).");
                    String passFood = MenuScanner.next();
                    System.out.println("Enter the passenger's row number (1 through " + passPlaneID.getRows() + ").");
                    int passRow = MenuScanner.nextInt();
                    System.out.println("Enter the passenger's seat number on row " + passRow + " (1 through " + passPlaneID.getNumPerRow() + ").");
                    int passSeat = MenuScanner.nextInt();
                    boolean Found = true;
                    System.out.println("-----------------------------");
                    if(passPlaneID == null) // If the plane does not exist
                    {
                        System.out.println("Plane not here.");
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                    else if (passPlaneID.getFull() == true) // If the plane chosen is full
                    {
                        Found = false;
                        System.out.println("That Plane is already full! Searching for Planes with the same destination and available seats...");
                        for (int u=0; u < PlaneArray.length-2; u++)
                        {
                            if ((PlaneArray[u].getDestination().equals(passPlaneID.getDestination())) == true & PlaneArray[u].getFull() != true & PlaneArray[u].getPlaneNum() != passPlaneID.getPlaneNum())
                            {
                                System.out.println("Plane " + PlaneArray[u].getPlaneNum() + " is also bound for " + PlaneArray[u].getDestination() + ". Here are the available seats.");
                                Found = true;
                                for (int j=0; j < passPlaneID.getRows(); j++)
                                {
                                    for(int k=0; k < passPlaneID.getNumPerRow(); k++)
                                    {
                                        if (passPlaneID.Bookings[j][k] == null) // Display all planes with the same location and available seats
                                        {
                                            int addJ = j+1;
                                            int addK = k+1;
                                            System.out.println("Row " + addJ + ", Seat " + addK + ".");
                                        }
                                    }
                                }
                                System.out.println("-----------------------------");
                                displayMenu();
                                break;
                            }
                        }
                        if (Found == false) // If no planes with same destination were found
                        {
                            System.out.println("I was not able to find a Plane with the same destination, " + passPlaneID.getDestination() + ".");
                            System.out.println("-----------------------------");
                            displayMenu();
                            break;
                        }
                        break;
                    }
                    else if (passRow >= 1 & passSeat >= 1 & passRow <= passPlaneID.getRows() & passSeat <= passPlaneID.getNumPerRow()) // If the row and seat are valid
                    {
                        if(passPlaneID.Bookings[passRow-1][passSeat-1] == null) // If the valid seat is empty
                        {
                            Passenger pass = new Passenger(passName, passFood);
                            passPlaneID.setBookings(pass, passRow-1, passSeat-1);
                            System.out.println("Passenger " + passName + " added to " + passPlaneID.getPlaneNum() + " with food preference " + passFood + " on row " + passRow + ", seat " + passSeat + ".");
                            System.out.println("-----------------------------");
                            displayMenu();
                            break;
                        }
                    }
                    else
                    {
                        System.out.println("That seat is already taken or doesn't exist! Here is a list of seats on Plane " + passPlaneID.getPlaneNum() + " that are available:\n");
                        for (int g=0; g < passPlaneID.getRows(); g++)
                        {
                            for(int h=0; h < passPlaneID.getNumPerRow(); h++)
                            {
                                if (passPlaneID.Bookings[g][h] == null) // Shows available seating if the seat chosen was not valid
                                {
                                    int addG = g+1;
                                    int addH = h+1;
                                    System.out.println("Row " + addG + ", Seat " + addH + ".");
                                }
                            }
                        }
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                
                case 1: // Prints the sorted list of Planes.
                    System.out.println("-----------------------------");
                    printArray(PlaneArray);
                    System.out.println("-----------------------------");
                    displayMenu();
                    break;
                    
                case 2: // Asks for a specific plane, then displays all passengers on that plane.
                    System.out.println("Enter a Plane ID to display passengers for.");
                    Plane passID = searchPlane(PlaneArray, MenuScanner.nextInt());
                    System.out.println("-----------------------------");
                    if(passID == null)
                    {
                        System.out.println("Plane not here.");
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                    else
                    {
                        for(int b=0; b < passID.getRows(); b++)
                        {
                            for(int c=0; c < passID.getNumPerRow(); c++)
                            {
                                if (passID.Bookings[b][c] == null)
                                {
                                }
                                else
                                {
                                    System.out.println(passID.Bookings[b][c].passengerToString());
                                }
                            }
                        }
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }            
                
                case 3: // Displays food count for a plane
                    System.out.println("Enter a Plane ID to display food count for.");
                    Plane foodID = searchPlane(PlaneArray, MenuScanner.nextInt());
                    System.out.println("-----------------------------");
                    if(foodID == null) // If the plane chosen does not exist
                    {
                        System.out.println("Plane not here.");
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                    else
                    {
                        int chicken = 0;
                        int pasta = 0;
                        int special = 0;
                        int snack = 0;
                        String sc = "chicken";
                        String sp = "pasta";
                        String ss = "special";
                        for(int e=0; e < foodID.getRows(); e++)
                        {
                            for(int f=0; f < foodID.getNumPerRow(); f++)
                            {
                                if (foodID.getHasMeal() == true) // If the plane provides meals, count each meal found.
                                {
                                    if (foodID.Bookings[e][f] == null)
                                    {
                                    }
                                    else
                                    {
                                        if ((foodID.Bookings[e][f].getFoodPreference().equals(sc)) == true)
                                        {
                                            chicken = chicken + 1;
                                        }
                                        else if ((foodID.Bookings[e][f].getFoodPreference().equals(sp)) == true)
                                        {
                                            pasta = pasta + 1;
                                        }
                                        else if ((foodID.Bookings[e][f].getFoodPreference().equals(ss)) == true)
                                        {
                                            special = special + 1;
                                        }
                                    }
                                }
                                else if(foodID.getHasMeal() == false) // If the plane doesn't provide meals, count every food preference as a snack.
                                {
                                    if (foodID.Bookings[e][f] == null)
                                    {
                                    }
                                    else
                                    {
                                        snack = snack + 1;
                                    }
                                }
                            }
                        }
                        if (foodID.getHasMeal() == false)
                        {
                            System.out.println("Snacks: " + snack);
                        }
                        else if(foodID.getHasMeal() == true)
                        {
                            System.out.println("Chicken: " + chicken + "\nPasta: " + pasta + "\nSpecials: " + special);
                        }
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                
                case 4: // Search for a passenger
                    System.out.println("Enter a Plane ID for passenger lookup.");
                    Plane searchID = searchPlane(PlaneArray, MenuScanner.nextInt());
                    System.out.println("-----------------------------");
                    System.out.println("Enter a passenger name to look for.");
                    String searchName = MenuScanner.next();
                    System.out.println("-----------------------------");
                    if(searchID == null) // If a plane is not found, say Plane not here.
                    {
                        System.out.println("Plane not here.");
                        System.out.println("-----------------------------");
                        displayMenu();
                        break;
                    }
                    else
                    {
                        boolean Success = false;
                        for(int q=0; q < searchID.getRows(); q++)
                        {
                            for(int r=0; r < searchID.getNumPerRow(); r++)
                            {
                                if ((searchID.Bookings[q][r] == null))
                                {
                                }
                                else if ((searchID.Bookings[q][r].getName().equals(searchName)) == true) // If a passenger with the same name is found
                                {
                                    System.out.println("Passenger found.");
                                    int searchRow = q + 1;
                                    int searchSeat = r +1;
                                    System.out.println("Passenger " + searchID.Bookings[q][r].getName() + " is sitting on row " + searchRow + ", seat " + searchSeat + ".");
                                    System.out.println("-----------------------------");
                                    Success = true;
                                    displayMenu();
                                    break;
                                }
                            }
                        }
                        if (Success == false) // If a passenger is not found
                        {
                            System.out.println("Passenger not here.");
                            System.out.println("-----------------------------");
                            displayMenu();
                            break;
                        }
                        break;
                    }
                
                case 5: // Searches for a Plane using binary search.
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
                
                case 6: // Exit if the user wishes to exit.
                    System.out.println("-----------------------------");
                    System.out.println("Exiting.");
                    System.out.println("-----------------------------");
                    running = false;
                    break;
            }
        }
        MenuScanner.close(); // Close scanner.
    }
    public static void displayMenu() // Prints the menu.
    {
        System.out.println("Please enter one of the following.\n" + "0: Add Passenger\n" + "1: List Planes\n" + "2: List Passengers\n" + "3: Display Food Count\n" + "4: Find Passenger\n" + "5: Find Plane\n" + "6: Exit\n"); 
    }
    public static Plane[] PlaneFileReader() throws IOException
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
    public static void makeBookings(Plane PlaneArray[]) throws IOException
    {
        Scanner sf = new Scanner(new File("bookings.txt")); // Collects and reads the planes.txt file. This was included in the zip, so the directory should work.
        String spArray[];
        String x;
        int maxIndx = -1;
        String text[] = new String[50000];
        
        while(sf.hasNext())
        {
            maxIndx++;
            text[maxIndx] = sf.nextLine();
        }
        sf.close(); // Closes the text file scanner.
        
        for(int j=1; j <= 1836; j++) // By starting at line 1 instead of 0, the string skips the header.
        {
            x = text[j];
            spArray = x.split(","); // Splits the string, removing commas and inserting the rest into an array.
            int PassPlane = Integer.parseInt(spArray[0]);
            String Name = spArray[1];
            String FoodPreference = spArray[2];
            int Row = Integer.parseInt(spArray[3]);
            int Seat = Integer.parseInt(spArray[4]);
            Passenger p = new Passenger(Name, FoodPreference);
            for(int a=0; a <= PlaneArray.length-2; a++) // Creates each booking. Duplicates are overwritten.
            {
                if (PassPlane == PlaneArray[a].getPlaneNum())
                {
                    if (Row <= PlaneArray[a].getRows() & Seat <= PlaneArray[a].getNumPerRow())
                    {
                        PlaneArray[a].setBookings(p, Row-1, Seat-1);
                    }
                }
            }
        }
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
    public static void analyzeAndSetTakenSeats(Plane PlaneArray[]) // Sets the amount of seats taken on a plane. This is used to check if a plane is full.
    {
        for(int i=0; i < PlaneArray.length-1; i++)
        {
            int BookingCount = 0;
            for(int j=0; j < PlaneArray[i].getRows(); j++)
            {
                for(int k=0; k < PlaneArray[i].getNumPerRow(); k++)
                {
                    if (PlaneArray[i].Bookings[j][k] == null)
                    {
                    }
                    else
                    {
                        BookingCount = BookingCount + 1;
                        PlaneArray[i].setSeatsTaken(BookingCount);
                    }
                }
            }
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
