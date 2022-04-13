Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\James The Gamer\AppData\Local\Programs\Python\Python39\Scripts\prog1main.py
----------------------------------------------
One moment, please. Inserting text from prog1input1.txt into a Linked List...
Done.
One moment, please. Inserting text from prog1input2.txt into a Linked List...
Done.
----------------------------------------------

Please enter the file input you would like to search through (1 or 2) or type "exit" to exit: 1
Please enter the pattern you would like to search for: Ickle
Searching for Pattern: Ickle

----------------------------------------------
Starting Brute Force search...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (Ickle): 8
Potential Character Matches Explored: 42
Total Comparisons: 485
Total Time Taken: 0.0 seconds
Theoretical Time Complexity: O(mn)
Conclusion: Although brute force would occassionally result in *slightly* faster times, the difference to KMP was usually minimal, and KMP would have less comparisons. Brute force does do adequately here due to the smaller patterns, but for bigger ones could struggle.
----------------------------------------------
Initializing Knuth-Morris-Pratt...
Creating failure function...
Done. Failure Function:

Ickle
00000

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (Ickle): 8
Potential Character Matches Explored: 42
Total Comparisons: 485
Total Time Taken: 0.011002302169799805 seconds
Theoretical Time Complexity: O(n)
Conclusion: Although KMP would occasionally be slower than brute force, the difference was small enough to be ignored entirely, and KMP had less comparisons. On average, KMP will be the best bet, although its preprocessing with the creation of the Failure Function is something to consider.
----------------------------------------------
Initializing Boyer-Moore...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (Ickle): 8
Potential Character Matches Explored: 112
Total Comparisons: 225
Total Time Taken: 0.0010080337524414062 seconds
Theoretical Time Complexity: Average O(n), Worst Case O(mn)
Conclusion: Despite it having the lowest amount of total search comparisons, Boyer-Moore had the highest time taken by far. This is largely due to the massively inefficient process of sifting through the Linked Lists each time to work backwards. This could be largely alleviated by the alternate method discussed in the PowerPoint utilizing tables for the Bad Symbols and Good Suffixes.
----------------------------------------------


Please enter the file input you would like to search through (1 or 2) or type "exit" to exit: 1
Please enter the pattern you would like to search for: toot
Searching for Pattern: toot

----------------------------------------------
Starting Brute Force search...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (toot): 0
Potential Character Matches Explored: 39
Total Comparisons: 487
Total Time Taken: 0.0010006427764892578 seconds
Theoretical Time Complexity: O(mn)
Conclusion: Although brute force would occassionally result in *slightly* faster times, the difference to KMP was usually minimal, and KMP would have less comparisons. Brute force does do adequately here due to the smaller patterns, but for bigger ones could struggle.
----------------------------------------------
Initializing Knuth-Morris-Pratt...
Creating failure function...
Done. Failure Function:

toot
0001

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (toot): 0
Potential Character Matches Explored: 39
Total Comparisons: 473
Total Time Taken: 0.017589330673217773 seconds
Theoretical Time Complexity: O(n)
Conclusion: Although KMP would occasionally be slower than brute force, the difference was small enough to be ignored entirely, and KMP had less comparisons. On average, KMP will be the best bet, although its preprocessing with the creation of the Failure Function is something to consider.
----------------------------------------------
Initializing Boyer-Moore...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (toot): 0
Potential Character Matches Explored: 6
Total Comparisons: 127
Total Time Taken: 0.0 seconds
Theoretical Time Complexity: Average O(n), Worst Case O(mn)
Conclusion: Despite it having the lowest amount of total search comparisons, Boyer-Moore had the highest time taken by far. This is largely due to the massively inefficient process of sifting through the Linked Lists each time to work backwards. This could be largely alleviated by the alternate method discussed in the PowerPoint utilizing tables for the Bad Symbols and Good Suffixes.
----------------------------------------------


Please enter the file input you would like to search through (1 or 2) or type "exit" to exit: 2
Please enter the pattern you would like to search for: mmmmm
Searching for Pattern: mmmmm

----------------------------------------------
Starting Brute Force search...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (mmmmm): 17448
Potential Character Matches Explored: 106435
Total Comparisons: 124888
Total Time Taken: 0.0200040340423584 seconds
Theoretical Time Complexity: O(mn)
Conclusion: Although brute force would occassionally result in *slightly* faster times, the difference to KMP was usually minimal, and KMP would have less comparisons. Brute force does do adequately here due to the smaller patterns, but for bigger ones could struggle.
----------------------------------------------
Initializing Knuth-Morris-Pratt...
Creating failure function...
Done. Failure Function:

mmmmm
01234

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (mmmmm): 17448
Potential Character Matches Explored: 95929
Total Comparisons: 114382
Total Time Taken: 0.04200935363769531 seconds
Theoretical Time Complexity: O(n)
Conclusion: Although KMP would occasionally be slower than brute force, the difference was small enough to be ignored entirely, and KMP had less comparisons. On average, KMP will be the best bet, although its preprocessing with the creation of the Failure Function is something to consider.
----------------------------------------------
Initializing Boyer-Moore...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (mmmmm): 17448
Potential Character Matches Explored: 90227
Total Comparisons: 94515
Total Time Taken: 61.75391864776611 seconds
Theoretical Time Complexity: Average O(n), Worst Case O(mn)
Conclusion: Despite it having the lowest amount of total search comparisons, Boyer-Moore had the highest time taken by far. This is largely due to the massively inefficient process of sifting through the Linked Lists each time to work backwards. This could be largely alleviated by the alternate method discussed in the PowerPoint utilizing tables for the Bad Symbols and Good Suffixes.
----------------------------------------------


Please enter the file input you would like to search through (1 or 2) or type "exit" to exit: 2
Please enter the pattern you would like to search for: mmmom
Searching for Pattern: mmmom

----------------------------------------------
Starting Brute Force search...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (mmmom): 0
Potential Character Matches Explored: 69809
Total Comparisons: 105711
Total Time Taken: 0.015002965927124023 seconds
Theoretical Time Complexity: O(mn)
Conclusion: Although brute force would occassionally result in *slightly* faster times, the difference to KMP was usually minimal, and KMP would have less comparisons. Brute force does do adequately here due to the smaller patterns, but for bigger ones could struggle.
----------------------------------------------
Initializing Knuth-Morris-Pratt...
Creating failure function...
Done. Failure Function:

mmmom
01201

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (mmmom): 0
Potential Character Matches Explored: 26137
Total Comparisons: 62039
Total Time Taken: 0.033098697662353516 seconds
Theoretical Time Complexity: O(n)
Conclusion: Although KMP would occasionally be slower than brute force, the difference was small enough to be ignored entirely, and KMP had less comparisons. On average, KMP will be the best bet, although its preprocessing with the creation of the Failure Function is something to consider.
----------------------------------------------
Initializing Boyer-Moore...

Search complete.
Length of Main Text: 35905
Total Full Pattern Matches (mmmom): 0
Potential Character Matches Explored: 19777
Total Comparisons: 42450
Total Time Taken: 16.804023265838623 seconds
Theoretical Time Complexity: Average O(n), Worst Case O(mn)
Conclusion: Despite it having the lowest amount of total search comparisons, Boyer-Moore had the highest time taken by far. This is largely due to the massively inefficient process of sifting through the Linked Lists each time to work backwards. This could be largely alleviated by the alternate method discussed in the PowerPoint utilizing tables for the Bad Symbols and Good Suffixes.
----------------------------------------------


Please enter the file input you would like to search through (1 or 2) or type "exit" to exit: exit
>>> 