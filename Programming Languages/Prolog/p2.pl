/*
Name: 		  	James Brooks
Date: 		  	February 20th, 2022
Course:		  	CSC 330-002
Quarter:	  		Winter Quarter 2021-2022
Project 2: 		Option B, Prolog Math
*/

/* Calculates the distance between two vectors and unifies the distance with R. */
/* Distance is calculated by taking the 1 dimensional distance for each coordinate point, squaring and adding each, and taking
   the square root of the sum. */
dist((X1,Y1,Z1),(X2,Y2,Z2),R) :- R is sqrt((X2-X1)**2+(Y2-Y1)**2+(Z2-Z1)**2).

/* Calculates the length of a single vector and unifies the length with R. */
/* Length is calculated by squaring and adding each coordiante point, and taking the square root of the sum. */
/* This function is used in other calculations, such as vecNorm and vecAngle. */
vecLength((X,Y,Z),R) :- R is sqrt(X**2+Y**2+Z**2).

/* Calculates the normal of a single vector and unifies the normalized vector with R. */
/* A normal vector is calculated by dividing each coordinate point by the vector's length. */
vecNorm((X,Y,Z),R) :- 
	vecLength((X,Y,Z),SS), 
	X1 is X/SS, 
	Y1 is Y/SS, 
	Z1 is Z/SS, 
	R = (X1,Y1,Z1).

/* Calculates the dot product of two vectors and unifies the result with R. */
/* Dot product is calculated by multiplying each respective coordinate point and adding them all together. */
vecDot((X1,Y1,Z1),(X2,Y2,Z2),R) :- R is (X1*X2+Y1*Y2+Z1*Z2).

/* Calculates the angle between two vectors in radians, and unifies the angle with R. */
/* The angle between two vectors is calculated by taking the dot product of two vectors, dividing by the lengths of the two vectors
   multiplied by one another, and taking the inverse cosine of that result. */
vecAngle((X1,Y1,Z1),(X2,Y2,Z2),R) :- 
	vecDot((X1,Y1,Z1),(X2,Y2,Z2),D), 
	vecLength((X1,Y1,Z1),SS1), 
	vecLength((X2,Y2,Z2),SS2), 
	R is acos(D/(SS1*SS2)).

/* Returns true if two vectors are orthogonal to one another, or false otherwise. */
/* Two vectors are orthogonal if their dot product is equal to zero. */
areOrthog((X1,Y1,Z1),(X2,Y2,Z2)) :- 
	vecDot((X1,Y1,Z1),(X2,Y2,Z2),D), D =:= 0.

/* Alternatively, two vectors are orthogonal if the angle between them is equal to pi/2 radians. */	
areOrthog2((X1,Y1,Z1),(X2,Y2,Z2)) :- 
	vecAngle((X1,Y1,Z1),(X2,Y2,Z2),A), A =:= pi/2.

/* Calculates the cross product of two vectors and unifies the cross product with R. */
/* Cross product is done by cross multiplying two columns at a time. The column not used is the coordinate point that the result is for. */
/* The y coordinate (or in terms of ijk, î) is negative in the result of the cross product. */
/* Calls a helper function to handle the cross multiplication. */
vecCross((X1,Y1,Z1),(X2,Y2,Z2),R) :- 
	crossHelper(Y1,Z2,Z1,Y2,CX),
	crossHelper(X1,Z2,Z1,X2,Y),
	crossHelper(X1,Y2,Y1,X2,CZ),
	CY is Y * -1,
	R = (CX,CY,CZ).

/* Cross multiplying multiplies the top left with the bottom right, and subtracts the top right multiplied by the bottom left. */
crossHelper(V1,V2,V3,V4,R) :-
	R is (V1*V2-V3*V4).

/* Calculates the vector projection of the first argument onto the second argument, and unifies the projection with R. */
/* Projection is found by dividing the dot product of the two vectors by the length of the vector being projected onto,
   then by multiplying that value by each coordinate of the vector being projected onto divided by the length. */
vecProj((X1,Y1,Z1),(X2,Y2,Z2),R) :-
	vecDot((X1,Y1,Z1),(X2,Y2,Z2),D),
	vecLength((X2,Y2,Z2),U),
	C is (D/U),
	PX is (X2/U*C),
	PY is (Y2/U*C),
	PZ is (Z2/U*C),
	R = (PX,PY,PZ).

/* Calculates the distance from a point off of a line (P1) to a line, utilizing P1, a point on the line (P2), and a vector parallel to the line (V). */
/* R is unified with the distance. */
/* Distance is found by first creating a new vector from the point in space to the point on the line. */
/* Our new vector is then cross product with the vector parallel to the line, and the magnitude (length) of this vector is found. */
/* That magnitude is then divided by the magnitude of the original vector parallel to the line to finally get the distance. */
distPointLine((P1X,P1Y,P1Z),(VX,VY,VZ),(P2X,P2Y,P2Z),R) :-
	getVector((P1X,P1Y,P1Z),(P2X,P2Y,P2Z),N),
	vecCross(N,(VX,VY,VZ),C),
	vecLength(C,CM),
	vecLength((VX,VY,VZ),VM),
	R is (CM/VM).

/* Used to make a vector given a starting and end point. */
/* The starting point's coordinates are subtracted from the ending point's to get the vector. */
getVector((P1X,P1Y,P1Z),(P2X,P2Y,P2Z),V) :-
	VX is P2X - P1X,
	VY is P2Y - P1Y,
	VZ is P2Z - P1Z,
	V = (VX,VY,VZ).

/* Calculates the distance from a point off of a plane (P1) to a plane, utilizing P1, a point on the plane (P2), and a vector normal to the plane (N). */
/* R is unified with the distance. */
/* Distance is found by first crating a new vector from the point on the plane to the point in space. */
/* Our new vector is then dot product with the vector normal to the plane. */
/* That vector is then divided by the length of the vector normal to the plane to get the distance. */
distPointPlane((P1X,P1Y,P1Z),(NX,NY,NZ),(P2X,P2Y,P2Z),R) :-
	getVector((P2X,P2Y,P2Z),(P1X,P1Y,P1Z),V),
	vecDot(V,(NX,NY,NZ),D),
	vecLength((NX,NY,NZ),L),
	R is (D/L).