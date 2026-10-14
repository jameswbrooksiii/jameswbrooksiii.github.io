
/**
 * The Plane Class.
 *
 * James Brooks
 * Date
 */

// The Plane Class
public class Plane
{
    // instance variables
    private int PlaneNum;
    private String Destination;
    private int DayOfTravel;
    private String Meal;
    private int Rows;
    private int NumPerRow;

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
        this.Rows = 0;
        this.NumPerRow = 0;
    }
    public Plane(int PlaneNum, String Destination, int DayOfTravel, String Meal, int Rows, int NumPerRow)
    {
        this.PlaneNum = PlaneNum;
        this.Destination = Destination;
        this.DayOfTravel = DayOfTravel;
        this.Meal = Meal;
        this.Rows = Rows;
        this.NumPerRow = NumPerRow;
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
    public int getRows()
    {
        return this.Rows;
    }
    public int getNumPerRow()
    {
        return this.NumPerRow;
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
    public void setRows(int Rows)
    {
        this.Rows = Rows;
    }
    public void setNumPerRow(int NumPerRow)
    {
        this.NumPerRow = NumPerRow;
    }
    public String toString() // Returns a String of the values of a Plane.
    {
        return PlaneNum + ", " + Destination + ", " + DayOfTravel + ", " + Meal + ", " + Rows + ", " + NumPerRow;
    }
}
      

    