/*
Name: 		  	James Brooks
Date: 		  	February 7th, 2022
Course:		  	CSC 330-002
Quarter:	  	Winter Quarter 2021-2022
Assignment #: 	Assignment #6
*/

/* Function takes input and output txt files. get/1 gets the next non-white space character in the file and returns its ASCII code. */
/* If at end of file, get/1 returns -1. Passes the read character to process helper function, along with 0, the currently empty sum. */
/* When process is done, print the sum and close streams. */
intsum(Infile, Outfile) :- see(Infile), tell(Outfile), get(X), process(X,0,R), write(R), nl, seen, told.

/* If at the end of file, unify with the current sum. */
process(-1,Y,Y).
/* Double check to make sure we aren't at the end of the file. Convert the char_code to a "normal" integer by subtracting the char_code by 48. */
/* Add the integer to the current sum. Get the next char, and run again. */
process(X,Y,R) :- X \= -1, I is X - 48, Y1 is I + Y, get(X1), process(X1,Y1,R).