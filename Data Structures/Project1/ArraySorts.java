/*******************************
 * TO DO:
 * 
 * Read the code to understand how arrays work in Java and the basics for Strings
 * Then determine who Larry, Moe, and Curly are in this context. 
 * One is a selection sort, one is a bubble sort, and one is an insertion sort.
 * 
 * Once you've figured that out, go take to quiz to unlock the notes for this lesson.
 */


//the most common libraries you'll need
import java.io.*; 
import java.util.*;

public class ArraySorts
{
    public static void main (String[] args)
    {
        String[] s = new String[9]; //creates the array
        
        //put some data in it now
        s[0] = "Kirk";
        s[1] = "McCoy";
        s[2] = "Spock";
        s[3] = "Picard";
        s[4] = "Riker";
        s[5] = "Janeway";
        s[6] = "Tuvok";
        s[7] = "Sisko";
        s[8] = "Dax";
                
        //oops! McCoy doesn't belong in that list!
        for (int i = 1; i < s.length - 2; i++) //why length - 2???
        {
            s[i] = s[i+1];
        }
        s[8] = "";
        
        //uncomment one at a time to run these sorting algorithms
        //Larry(s);
        //Moe(s);
        //Curly(s);
        
    }
    
    public static void Larry(String[] arr) // note: you only need "static" for methods called in the same class that main is in
    {
        int n = arr.length; 
        for (int i = 1; i < n; i++) { 
            String key = arr[i]; 
            int j = i - 1; 
  
            while (j >= 0 && arr[j].compareTo(key) > 0) { 
                arr[j + 1] = arr[j]; 
                j = j - 1; 
            } 
            arr[j + 1] = key; 
        } 
    }
    
    public static void Moe(String[] arr)
    {
        int n = arr.length; 
  
        for (int i = 0; i < n-1; i++) 
        { 
            int min_idx = i; 
            for (int j = i+1; j < n; j++) 
                if (arr[j].compareTo(arr[min_idx]) < 0) 
                    min_idx = j; 
  
            String temp = arr[min_idx]; 
            arr[min_idx] = arr[i]; 
            arr[i] = temp; 
        } 
    }
    
    public static void Curly(String[] arr)
    {
        int n = arr.length; 
        for (int i = 0; i < n-1; i++) 
            for (int j = 0; j < n-i-1; j++) 
                if (arr[j].compareTo(arr[j+1]) > 0) 
                { 
                    String temp = arr[j]; 
                    arr[j] = arr[j+1]; 
                    arr[j+1] = temp; 
                } 
    }
}