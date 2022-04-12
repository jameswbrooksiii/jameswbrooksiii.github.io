
/**
 * Write a description of class Word here.
 *
 * James Brooks
 */
public class Word
{
    // instance variables - replace the example below with your own
    private String actualWord;
    private int samewordCount;

    /**
     * Constructor for objects of class Word
     */
    public Word()
    {
        // initialise instance variables
        this.actualWord = "";
        this.samewordCount = 1;
    }
    public Word(String actualWord)
    {
        this.actualWord = actualWord;
        this.samewordCount = 1;
    }

    public String getactualWord()
    {
        return this.actualWord;
    }
    public int getsamewordCount()
    {
        return this.samewordCount;
    }
    
    public void setactualWord(String actualWord)
    {
        this.actualWord = actualWord;
    }
    public void setsamewordCount()
    {
        this.samewordCount++;
    }
}
