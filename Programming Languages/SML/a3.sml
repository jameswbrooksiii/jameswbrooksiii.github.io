(*
Name: 			James Brooks
Date: 			December 20, 2021
Course: 		CSC 330-002
Quarter: 		Winter Quarter 2021-2022
Assignment #: 	Assignment #3
*)

(* Opens structures necessary for fromString and openIn functions *)
open TextIO;
open Int;

(* Function for adding the numbers from the file into a total *)
fun fadd([]) = 0
	| fadd (SOME x::xs) = x+fadd(xs) (* If the current item is some integer, add it to the total *)
	| fadd (NONE::xs) = fadd(xs); (* If NONE, skip and go to next item *)

(* Converts a string option to a string *)
fun fconvert(NONE) = ""
	| fconvert(SOME x) = x; (* Useful for putting the object from inputLine (originally a string option) into fromString (only takes string type) *)

(* Reads the file given to it and inputs information line by line into a list to be passed to fadd *)
fun fread (file, nums) = 
	if TextIO.endOfStream(file) = false (* If not at the end of the function, *)
		then fread(file, Int.fromString(fconvert(TextIO.inputLine(file)))::nums) (* Read line by line, then convert to string, and translate to integer before inserting into list *)
	else fadd(nums); (* If at the end of the file, pass the list to the fadd function *)

(* Main Function *)
(* Opens file name inputted into the function in the command line and passes it and an empty list to the fread function *)
fun fsum "" = 0
	| fsum file = fread(TextIO.openIn(file), []);