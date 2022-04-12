
/**
 * Write a description of class PostfixConverter here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.io.*;
import java.util.*;
public class PostfixConverter
{
    // instance variables - replace the example below with your own
    public static void main(String[] args)
    {
        String postfix = new String("");
        String values = new String("");
        int result = 0;
        postfix = PostfixConverter();
        values = GetValues(postfix);
        result = Calculate(values);
        System.out.println(postfix);
        System.out.println(values);
        System.out.println(result);
    }
    /**
     * Constructor for objects of class PostfixConverter
     */
    public static String PostfixConverter()
    {
        // initialise instance variables
        Scanner infixscanner = new Scanner(System.in);
        System.out.println("Please type an equation.");
        String infix = infixscanner.next();
        infixscanner.close();
        Stack<Character> stack = new Stack<>();
        String postfix = new String("");
        int count = 0;
        for(int i = 0; i < infix.length(); i++)
        {
            if(Character.isLetterOrDigit(infix.charAt(i)) == true)
            {
                postfix += infix.charAt(i);
            }
            else if (infix.charAt(i) == '(')
            {
                stack.push(infix.charAt(i));
            }
            else if (infix.charAt(i) == ')')
            {
                while (stack.peek() != '(')
                {
                    postfix += stack.peek();
                    stack.pop();
                }
                stack.pop();
            }
            else
            {
                if (stack.IsEmpty() == true)
                {
                    stack.push(infix.charAt(i));
                }
                else
                {
                    while ((infix.charAt(i) == '+' || infix.charAt(i) == '-') == true)
                    {
                        if (stack.peek() == null)
                        {
                            break;
                        }
                        else if (stack.peek() == '(')
                        {
                            break;
                        }
                        //else if(((stack.peek() == '/' || stack.peek() == '*') == true))
                        //{
                            //postfix += stack.peek();
                            //stack.pop();
                        //}
                        else
                        {
                            postfix += stack.peek();
                            stack.pop();
                        }
                    }
                    stack.push(infix.charAt(i));
                }
            }
        }
        while (stack.IsEmpty() != true)
        {
            if(stack.peek() == null)
            {
                break;
            }
            else
            {
                postfix += stack.peek();
                stack.pop();
            }
        }
        return(postfix);
    }
    
    public static String GetValues(String postfix)
    {
        String result = new String("");
        result = postfix;
        for(int i = 0; i < result.length(); i++)
        {
            if(Character.isLetter(result.charAt(i)) == true)
            {
                char var = result.charAt(i);
                System.out.println("What does " + result.charAt(i) + " equal?");
                Scanner valscanner = new Scanner(System.in);
                String val = valscanner.next();
                valscanner.close();
                for(int j = 0; j < result.length(); j++)
                {
                    if (result.charAt(j) == var)
                    {
                        result = result.substring(0, j)+ val + result.substring(j+1);
                    }
                }
            }
        }
        return result;
    }
    
    public static int Calculate(String values)
    {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        for(int i = 0; i < values.length(); i++)
        {
            if(Character.isDigit(values.charAt(i)) == true)
            {
                int funee = Character.getNumericValue(values.charAt(i));
                stack.push(funee);
            }
            else
            {
                int second = stack.peek();
                stack.pop();
                int first = stack.peek();
                stack.pop();
                if(values.charAt(i) == '+')
                {
                    stack.push(first+second);
                }
                else if(values.charAt(i) == '-')
                {
                    stack.push(first-second);
                }
                else if(values.charAt(i) == '*')
                {
                    stack.push(first*second);
                }
                else if(values.charAt(i) == '/')
                {
                    stack.push(first/second);
                }
            }
        }
        answer = stack.peek();
        return answer;
    }
}
