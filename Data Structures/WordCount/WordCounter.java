
/**
 * Write a description of class WordCounter here.
 *
 * James Brooks
 */
import java.io.*;
import java.util.*;
public class WordCounter
{
    // instance variables - replace the example below with your own
    /**
     * Constructor for objects of class WordCounter
     */
    public static void main(String[] args) throws Exception
    {
        // initialise instance variables
        File File = new File("paragraph.txt");
        List<Word> SortedList = FileScanner(File);
        WriteReport(SortedList);
    }
    public static List<Word> FileScanner(File File) throws IOException
    {
        Scanner sf = new Scanner(File);
        sf.useDelimiter("\\s+");
        String spArray[];
        String x;
        int maxIndx = -1;
        String text[] = new String[1000];
        List<Word> WordList = new List<Word>();
        
        while (sf.hasNext())
        {
            maxIndx++;
            text[maxIndx] = sf.nextLine();
        }
        sf.close();
        
        int TotalWords = 0;
        for(int j=0; j<=maxIndx; j++)
        {
            x = text[j];
            x = x.replaceAll("[\\t]", "");
            //spArray = x.split("\\. | \"|\" |, |: |\\s|; ");
            spArray = x.split("[,.:;\\s\"]+");
            int i = 0;
            while (i < spArray.length)
            {
                //System.out.println(spArray[i]);
                if (WordList.GetValue() != null)
                {
                    int z = 0;
                    while (z <= WordList.GetSize())
                    {
                        Word currWord = (Word)WordList.GetValue();
                        if ((spArray[i].equalsIgnoreCase(currWord.getactualWord())) == true )
                        {
                            currWord.setsamewordCount();
                            break;
                        }
                        else if ((z + 1) == WordList.GetSize())
                        {
                            Word uniqueword = new Word(spArray[i]);
                            WordList.InsertAfter(uniqueword);
                            break;
                        }
                        else
                        {
                            z++;
                            WordList.Next();
                        }
                    }
                    WordList.First();
                }
                else
                {
                    Word uniqueword = new Word(spArray[i]);
                    WordList.InsertAfter(uniqueword);
                }
                i++;
                TotalWords++;
            }
        }
        List<Word> SortedList = SortList(WordList);
        return SortedList;
    }
    public static List<Word> SortList(List<Word> WordList)
    {
        int n = WordList.GetSize();
        WordList.First();
        for (int i=0; i<n-1; i++)
        {
            for(int j=0; j<n-i-1; j++)
            {
                if(j<(n-1))
                {
                    WordList.SetPos(j);
                    Word firstword = (Word)WordList.GetValue();
                    int firstval = firstword.getsamewordCount();
                    WordList.Next();
                    Word secndword = (Word)WordList.GetValue();
                    int secndval = secndword.getsamewordCount();
                    if(firstval < secndval)
                    {
                        WordList.SetPos(j);
                        WordList.Replace(secndword);
                        WordList.Next();
                        WordList.Replace(firstword);
                    }
                }
            }
        }
        return WordList;
    }
    public static void WriteReport(List<Word> WordList) throws IOException
    {
        FileWriter fw = new FileWriter("Output.out");
        PrintWriter output = new PrintWriter(fw);
        
        WordList.First();
        int p = 0;
        int TotalWords = 0;
        output.println("WORD: TIMES USED");
        output.println("----------------");
        while (p < WordList.GetSize())
        {
            Word currWord = (Word)WordList.GetValue();
            output.print(currWord.getactualWord());
            output.print(": ");
            output.println(currWord.getsamewordCount());
            TotalWords += currWord.getsamewordCount();
            WordList.Next();
            p++;
        }
        output.println("");
        output.print("CREATIVITY RATIO: ");
        output.print(WordList.GetSize());
        output.print(" Unique Words/");
        output.print(TotalWords);
        output.print(" Total Words");
        output.close();
        fw.close();
    }
}
