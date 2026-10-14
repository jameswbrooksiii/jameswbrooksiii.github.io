
/**
 * The Passenger Class.
 *
 * James Brooks
 * @version (a version number or a date)
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
        this.Name = "empty";
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
}
