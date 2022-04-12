
/**
 * The Plane Class.
 *
 * James Brooks
 * 9/25/2020
 */

// The Plane Class
public class Plane
{
    // instance variables
    private int PlaneNum;
    private String Destination;
    private int DayOfTravel;
    private String Meal;
    private boolean HasMeal;
    private int Rows;
    private int NumPerRow;
    private int SeatsTaken;
    private int TotalSeats;
    private boolean Full;
    private String Status;
    Passenger Bookings[][] = new Passenger[Rows][NumPerRow];
    /**
     * Constructor for objects of class Plane
     */
    
    public Plane()
    {
        // initialise instance variables
        this.PlaneNum = 0;
        this.Destination = "";
        this.DayOfTravel = 0;
        this.Meal = "";
        this.HasMeal = false;
        this.Rows = 0;
        this.NumPerRow = 0;
        this.SeatsTaken = 0;
        this.TotalSeats = 0;
        this.Full = false;
        this.Status = "Plane not full.";
    }
    public Plane(int PlaneNum, String Destination, int DayOfTravel, String Meal, int Rows, int NumPerRow)
    {
        this.PlaneNum = PlaneNum;
        this.Destination = Destination;
        this.DayOfTravel = DayOfTravel;
        this.Meal = Meal;
        String s2 = "no";
        if((Meal.equals(s2)) == true)
        {
            HasMeal = false;
        }
        else if((Meal.equals(s2)) == false)
        {
            HasMeal = true;
        }
        this.Rows = Rows;
        this.NumPerRow = NumPerRow;
        this.SeatsTaken = SeatsTaken;
        this.TotalSeats = Rows * NumPerRow;
        if(SeatsTaken < TotalSeats)
        {
            this.Full = false;
            this.Status = "Plane not full.";
        }
        else
        {
            this.Full = true;
            this.Status = "PLANE FULL!";
        }
        this.Bookings = new Passenger[Rows][NumPerRow];
    }
    
    // Getters
    
    public int getPlaneNum()
    {
        return this.PlaneNum;
    }
    public String getDestination()
    {
        return this.Destination;
    }
    public int getDayOfTravel()
    {
        return this.DayOfTravel;
    }
    public String getMeal()
    {
        return this.Meal;
    }
    public boolean getHasMeal()
    {
        return this.HasMeal;
    }
    public int getRows()
    {
        return this.Rows;
    }
    public int getNumPerRow()
    {
        return this.NumPerRow;
    }
    public int getSeatsTaken()
    {
        return this.SeatsTaken;
    }
    public int getTotalSeats()
    {
        return this.TotalSeats;
    }
    public boolean getFull()
    {
        return this.Full;
    }
    public String getStatus()
    {
        return this.Status;
    }
    public Passenger[][] getBookings()
    {
        return this.Bookings;
    }
    
    // Setters
    
    public void setPlaneNum(int PlaneNum)
    {
        this.PlaneNum = PlaneNum;
    }
    public void setDestination(String Destination)
    {
        this.Destination = Destination;
    }
    public void setDayOfTravel(int DayOfTravel)
    {
        this.DayOfTravel = DayOfTravel;
    }
    public void setMeal(String Meal)
    {
        this.Meal = Meal;
    }
    public void setHasMeal(boolean HasMeal)
    {
        this.HasMeal = HasMeal;
    }
    public void setRows(int Rows)
    {
        this.Rows = Rows;
    }
    public void setNumPerRow(int NumPerRow)
    {
        this.NumPerRow = NumPerRow;
    }
    public void setSeatsTaken(int SeatsTaken)
    {
        this.SeatsTaken = SeatsTaken;
    }
    public void setTotalSeats(int TotalSeats)
    {
        this.TotalSeats = TotalSeats;
    }
    public void setFull(boolean Full)
    {
        this.Full = Full;
    }
    public void setStatus(String Status)
    {
        this.Status = Status;
    }
    public void setBookings(Passenger p, int Row, int Seat)
    {
        Bookings[Row][Seat] = p;
        this.Bookings = Bookings;
    }
    
    // toString
    
    public String toString() // Returns a String of the values of a Plane.
    {
        return PlaneNum + ", " + Destination + ", " + DayOfTravel + ", " + Meal + ", " + Rows + ", " + NumPerRow + ", " + SeatsTaken + "/" + TotalSeats + ": " + Status;
    }
}