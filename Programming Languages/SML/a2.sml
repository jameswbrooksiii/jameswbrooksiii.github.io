(*
Name: 			James Brooks
Date: 			December 16, 2021
Course: 		CSC 330-002
Quarter: 		Winter Quarter 2021-2022
Assignment #: 	Assignment #2
*)

fun optconcat [] = "" (* Base case: If empty list, returns "" *)
	| optconcat ((SOME x)::xs) = str(x)^optconcat(xs) (* If SOME char, make it a string, and concatenate it recursively with rest of the list *)
	| optconcat (NONE::xs) = optconcat(xs); (* If NONE, skip and go to the next item in list (Lecture 6 optsum) *)