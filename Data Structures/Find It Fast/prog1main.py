################
# James Brooks #
# Program 1    #
################

from linkedlist import *
import time

# ALL ALGORITHMS
############################################################################################################################################################################################################################################

# BRUTE FORCE #
def BF(LL, PL):
    print("Starting Brute Force search...")
    start = time.time()
    mcurrent = LL.head # The main pointer in the large string
    pcurrent = PL.head # The pattern pointer in the substring
    analyze = LL.head # Analyze is a third pointer that is used to move along the large string. Without it, "mmmmmm" when searching for "mmmmm" would return 1 instead of 2.
    c = 0 # Total comparisons
    m = 0 # Character matches
    p = 0 # Full pattern match
    
    while analyze != None:
        
        if (pcurrent.data == analyze.data): # If there is a character match,
            pcurrent = pcurrent.next # Move to the next pattern character
            analyze = analyze.next # Move down the main string, but keep mcurrent in the same place so we can go back to it
            c += 1 # Increase total comparisons
            m += 1 # Increase total matches
            
            if (pcurrent == None): # If we reach the end of the pattern, we found a full match!
                p += 1 # Increase full pattern matches
                pcurrent = PL.head # Go back to start of pattern substring
                mcurrent = mcurrent.next # Advance down the main string by 1 from where we left off (again, don't want to miss overlapping pattern matches)
                analyze = mcurrent

        else: # Character Mismatch
            c += 1 # Total comparisons increase
            pcurrent = PL.head
            mcurrent = mcurrent.next # In brute force, we only move down once!
            analyze = mcurrent

    end = time.time()
    print("\nSearch complete.")
    print("Length of Main Text: {}".format(len(text)))
    print("Total Full Pattern Matches ({}): {}".format(pattern, p))
    print("Potential Character Matches Explored: {}".format(m))
    print("Total Comparisons: {}".format(c))
    print("Total Time Taken: {} seconds".format(end-start))
    print("Theoretical Time Complexity: O(mn)")
    print("Conclusion: Although brute force would occassionally result in *slightly* faster times, the difference to KMP was usually minimal, and KMP would have less comparisons. Brute force does do adequately here due to the smaller patterns, but for bigger ones could struggle.")

# KNUTH-MORRIS-PRATT #
def KMP(LL, PL):
    print("----------------------------------------------\nInitializing Knuth-Morris-Pratt...")
    start = time.time()
    mcurrent = LL.head # The main pointer in the large string
    pcurrent = PL.head # The pattern pointer in the substring
    analyze = LL.head # Analyze is a third pointer that is used to move along the large string. Without it, "mmmmmm" when searching for "mmmmm" would return 1 instead of 2.
    c = 0 # Total comparisons
    m = 0 # Character matches
    p = 0 # Full pattern match

    # create failure function
    # Had help here from educative.io again: https://www.educative.io/edpresso/what-is-the-knuth-morris-pratt-algorithm
    print("Creating failure function...")
    FF = [0] * len(pattern)
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            FF[j] = i
            j += 1
        elif i == 0:
            FF[j] = 0
            j += 1
        else:
            i = FF[i-1]
    print("Done. Failure Function:\n")
    print("{}".format(pattern))
    for i in range(len(pattern)):
        print(FF[i], end = "")

    i = 0
    while analyze != None:
        c += 1  # Increase total comparisons by 1.
        
        if (pcurrent.data == analyze.data): # If we have a pattern match,
            pcurrent = pcurrent.next # Move the pattern pointer over by 1
            analyze = analyze.next # Move the analyze pointer down the main string 1 (not the same as the main string pointer)
            m += 1 # Increase character matches
            i += 1 # Increase counter (used for failure function)
            
            if (pcurrent == None): # Happens with full pattern match
                p += 1 # Increase full pattern match
                i = 0 # Set pattern progression counter back to zero
                pcurrent = PL.head # Reset pattern
                mcurrent = mcurrent.next # Move down main string by one
                analyze = mcurrent # Draw the analyze pointer back to the main one (again, this is used to catch all pattern matches, including overlaps)

        else: #If the characters do not match,
            pcurrent = PL.head # Reset the pattern regardless of what happens
            
            if i != 0: # If there was any progression down the pattern,
                i = FF[i-1] # Fetch the spaces needed to move from the Failure Function
                for j in range(i):
                    pcurrent = pcurrent.next # Move the pattern pointer down the spaces received from the failure function. If it came back zero, we are already at the pattern head.
                mcurrent = analyze # Moves the main pointer *up* to the analyze pointer. This is what actually reduces the redundant searches.

            else: # If we didn't find any current pattern matches,
                mcurrent = mcurrent.next # We are just going to move up once in the main string anyways.
                analyze = mcurrent

    end = time.time()
    print("\n\nSearch complete.")
    print("Length of Main Text: {}".format(len(text)))
    print("Total Full Pattern Matches ({}): {}".format(pattern, p))
    print("Potential Character Matches Explored: {}".format(m))
    print("Total Comparisons: {}".format(c))
    print("Total Time Taken: {} seconds".format(end-start))
    print("Theoretical Time Complexity: O(n)")
    print("Conclusion: Although KMP would occasionally be slower than brute force, the difference was small enough to be ignored entirely, and KMP had less comparisons. On average, KMP will be the best bet, although its preprocessing time with the creation of the Failure Function is something to consider.")

# BOYER-MOORE #
def BM(LL, PL):
    print("----------------------------------------------\nInitializing Boyer-Moore...")
    start = time.time()
    mcurrent = LL.head
    for i in range(len(pattern)-1): # Advance up in the main string at the start, since we are looking for the last character in the pattern
        mcurrent = mcurrent.next
    pcurrent = PL.tail # Set the current pointer in the pattern at the end rather than the beginning
    analyze = mcurrent
    i = len(pattern)
    k = 0 # Counter used for advancing
    c = 0 # Total comparisons
    m = 0 # Character matches
    p = 0 # Full pattern matches

    while mcurrent:
        
        if (pcurrent.data == mcurrent.data): # If we have a character match,
            if (pcurrent == PL.head): # Check if we are at the head. If we are, that's a full character match!
                p += 1 # Increase pattern match
                c += 1 # Increase comparisons
                m += 1 # Increase character match
                k = 0 # Reset counter (used for mismatch)
                pcurrent = PL.tail # Put pattern back at the end
                mcurrent = analyze # Move mcurrent up
                mcurrent = mcurrent.next # Then move down main string by one
                analyze = mcurrent

            else: # Character match, but not at head yet
                ptracker = pcurrent
                mtracker = mcurrent
                mcurrent = LL.head
                pcurrent = PL.head
                while pcurrent.next != ptracker: # Used to advance up the pattern from the beginning to the previous node
                    pcurrent = pcurrent.next
                while mcurrent.next != mtracker: # Used to advance up the main string from the beginning to the previous node
                    mcurrent = mcurrent.next
                c += 1 # Increase comparisons
                m += 1 # Increase character match
                k += 1 # Increase counter (used for mismatch)

        else: # Character mismatch!
            c += 1 # Increase comparisons
            j = 1 # (used for determining last seen character)
            i = len(pattern)
            
            ptracker = pcurrent
            pcurrent = PL.head
            lastc = 0
            while (pcurrent != None):
                if (pcurrent.data == mcurrent.data): # Search for the current character in the main text in our pattern to see if it appears earlier in the pattern.
                    lastc = j
                    j += 1
                    pcurrent = pcurrent.next
                else:
                    j += 1
                    pcurrent = pcurrent.next

            pcurrent = PL.head
            j = 1
            lasts = 0
            if (ptracker.next != None):
                while (pcurrent != None):
                    if (pcurrent.data == ptracker.next.data): # Search for the suffix in a progressed pattern to see if it appears earlier in the pattern.
                        lasts = j
                        j += 1
                        pcurrent = pcurrent.next
                    else:
                        j += 1
                        pcurrent = pcurrent.next

            if lasts != 0: # If there is a suffix,
                if lastc <= lasts:
                    shift = i - lastc # See if the suffix is worth implementing (i.e. more characters skipped)
                else:
                    shift = i - lasts
            else:
                shift = i - lastc # Otherwise, just use the last character
            mcurrent = analyze

            if shift == 0: # In the event that we reached the tail of the pattern,
                mcurrent = mcurrent.next # Move up the main text only once
                
            elif shift == len(pattern): # Otherwise, if shift stayed the same,
                shift = shift - k # Check to see if we progressed down the pattern, and if we did, we're not going to skip ahead as far.
                for i in range(shift):
                    if mcurrent != None:
                        mcurrent = mcurrent.next

            else: # Otherwise,
                for i in range(shift):
                    if mcurrent != None:
                        mcurrent = mcurrent.next # We are just going to move down the list by the full length of the pattern.

            analyze = mcurrent
            pcurrent = PL.tail # Set the pattern back to the tail.
            k = 0
            
    end = time.time()
    print("\nSearch complete.")
    print("Length of Main Text: {}".format(len(text)))
    print("Total Full Pattern Matches ({}): {}".format(pattern, p))
    print("Potential Character Matches Explored: {}".format(m))
    print("Total Comparisons: {}".format(c))
    print("Total Time Taken: {} seconds".format(end-start))
    print("Theoretical Time Complexity: Average O(n), Worst Case O(mn)")
    print("Conclusion: Despite it having the lowest amount of total search comparisons, Boyer-Moore had the highest time taken by far. This is largely due to the massively inefficient process of sifting through the Linked Lists each time to work backwards. This could be largely alleviated by the alternate method discussed in the PowerPoint utilizing tables for the Bad Symbols and Good Suffixes.")
    print("----------------------------------------------\n")

############################################################################################################################################################################################################################################

# MAIN CODE #

print("----------------------------------------------\nOne moment, please. Inserting text from prog1input1.txt into a Linked List...")
LL = LinkedList() # initializes a Linked List for the main text
text = open('prog1input1.txt', 'r').read() # opens the first file
for i in range(len(text)):
    LL.insert(text[i]) # inserts each character from the text as a node into the main text linked list
print("Done.")
print("One moment, please. Inserting text from prog1input2.txt into a Linked List...")
LL2 = LinkedList()
text = open('prog1input2.txt', 'r').read() # opens the second file
for i in range(len(text)):
    LL2.insert(text[i]) # inserts each character from the text as a node into the main text linked list
print("Done.\n----------------------------------------------")
searchin = True
while searchin == True:
    SL = input("\nPlease enter the file input you would like to search through (1 or 2) or type \"exit\" to exit: ")
    if SL == "exit":
        searchin == False
        break
    elif SL == "1":
        SSL = LL
    elif SL == "2":
        SSL = LL2
    pattern = input("Please enter the pattern you would like to search for: ")
    print("Searching for Pattern: {}\n\n----------------------------------------------".format(pattern))
    PL = LinkedList() # initializes a Linked List for the pattern substring
    for i in range(len(pattern)):
        PL.insert(pattern[i]) # inserts each character from the pattern as a node into the substring linked list

    # Running each algorithm with the given string and substring pattern
    BF(SSL, PL)
    KMP(SSL, PL)
    BM(SSL, PL)
