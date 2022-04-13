/*
Name: 		  	James Brooks
Date: 		  	January 24th, 2022
Course:		  	CSC 330-002
Quarter:	  	Winter Quarter 2021-2022
Assignment #: 	Assignment #4
*/

inv(
	item(bread),
	price(0.90),
	quantity(50)
).

inv(
	item(milk),
	price(2.50),
	quantity(30)
).

inv(
	item(cheese),
	price(1.50),
	quantity(80)
).

inv(
	item(chips),
	price(1.00),
	quantity(50)
).

inv(
	item(apples),
	price(0.30),
	quantity(100)
).

/* Add your predicates below here */

/* Item name is taken as the first argument. */
/* Once the item name is found, the second argument is matched with that item's price. */
/* Item quantity is ignored here. */
getPrice(X,Y) :- inv(
	item(X),
	price(Y),
	_
).

/* Item name is taken as the first argument. */
/* Once the item name is found, the second argument is matched with that item's quantity. */
/* Item price is ignored here. */
getQuantity(X,Y) :- inv(
	item(X),
	_,
	quantity(Y)
).

/* Runs getPrice for the first and second argument and matches the results to new variables. */
/* If the first variable is greater than the second, returns true. */
/* Otherwise, returns false. */
higherPrice(X,Y) :- getPrice(X,A), getPrice(Y,B), A>B.

/* Runs getPrice and getQuantity for the same item (first argument) and matches them to new variables. */
/* The second argument is matched with the price times the quantity to get gross. */
computeGross(X,G) :- getPrice(X,A), getQuantity(X,B), G is A*B.

/* Runs computeGross for the first and second argument and matches the results to new variables. */
/* If the first variable is greater than the second, returns true. */
/* Otherwise, returns false. */
higherGross(X,Y) :- computeGross(X,A), computeGross(Y,B), A>B.