
/**
 * The Passenger Class.
 *
 * James Brooks
 * 9/25/2020
 */

// The Passenger class
public class Passenger
{
    // instance variables - replace the example below with your own
    private String Name;
    private String FoodPreference;

    /**
     * Constructor for objects of class Passenger
     */
    public Passenger()
    {
        // initialise instance variables
        this.Name = "EMPTY";
        this.FoodPreference = "none";
    }
    public Passenger(String Name, String FoodPreference)
    {
        this.Name = Name;
        this.FoodPreference = FoodPreference;
    }
    
    // Getters
    
    public String getName()
    {
        return this.Name;
    }
    public String getFoodPreference()
    {
        return this.FoodPreference;
    }
    
    // Setters
    
    public void setName(String Name)
    {
        this.Name = Name;
    }
    public void setFoodPreference(String FoodPreference)
    {
        this.FoodPreference = FoodPreference;
    }
    
    // toString
    
    public String passengerToString()
    {
        return this.Name + ", " + this.FoodPreference;
    }
}