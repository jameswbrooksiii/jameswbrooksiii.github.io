/*
Name: 		  	James Brooks
Date: 		  	January 31st, 2022
Course:		  	CSC 330-002
Quarter:	  	Winter Quarter 2021-2022
Assignment #: 	Assignment #5
*/

/* myfun/2 has 3 main cases. */
/* The first two cases are used if the number equals one (unifies with 3) or if the number equals 2 (unifies with 4). */
myfun(1, 3).
myfun(2, 4).
/* The last occurs as long as the number given is greater than or equal to three. */
/* It recursively calls itself, adding the function to itself with the number minus one and the number minus two respectively. */
/* It calls this until it reaches the other two cases, where R is finally unified with the result of the addition. */
myfun(N, R) :- integer(N), N >= 3, A is N-1, B is N-2, myfun(A,X), myfun(B,Y), R is X+Y.
/* All other cases (numbers less than one) return false. */



/* fill/3 has two main cases. */
/* If the end number was reached (or if the start and end number were the same to begin with), add the current number to the list and end the list. */
fill(X,X,[X|[]]).
/* The other unifies R with a list. As long as the current number is less than the given end number, append the current number to the front of the list. */
/* Then, recursively call the function, increasing the current number by one. This is done until the first case is reached. */
fill(X,Y,[X|T]) :- X < Y, A is X+1, fill(A,Y,T).
/* All other cases (start number is higher than end number) return false. */ 