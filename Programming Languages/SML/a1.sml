(*
Name: 			James Brooks
Date: 			December 14, 2021
Course: 		CSC 330-002
Quarter: 		Winter Quarter 2021-2022
Assignment #: 	Assignment #1
*)

(* Commented out prototype that doesn't use pattern matching but achieves same result for the most part (throws a warning or two) *)
(*
fun apply (f, a) = 
	if (a=nil) 
		then nil 
	else f(hd(a))::apply(f,tl(a));
*)

(* Final result using pattern matching *)
fun apply (f,nil) = nil (* Base case for empty list. Returns nil ([]) *)
	| apply(f,x::xs) = f(x)::apply(f,xs); (* Everything else *)