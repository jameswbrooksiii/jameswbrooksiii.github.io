(*
Name: 			James Brooks
Date: 			January 21, 2022
Course: 		CSC 330-002
Quarter: 		Winter Quarter 2021-2022
Assignment #: 	Project #1
*)

(* Opens structures necessary for fromString and openIn functions *)
open TextIO;
open Int;

(* Converts int option to int. Useful because Int.fromString returns an int option. *)
fun intconvert(NONE) = 0
	| intconvert(SOME x) = x;

(* Takes the result of pcombine and evaluates it. *)
fun doit("", nums) = nums (* If there is an empty string from pcombine [no chars were stored], just return nums as it was. *)
	| doit(x, nums) = intconvert(Int.fromString(x))::nums; (* If there is a string, convert it to int option, then int, before putting it in the nums list. *)

(* Takes the list of chars and returns a string. *)
fun pcombine([]) = "" (* If empty list [no chars stored] returns empty string "". *)
	| pcombine(chars) = implode(chars); (* If chars are present, implode the chars into a single string. *)

(* Reorders any list from front to back to back to front. Because list inserts are right associative, to get things in the "correct" order, we must reorder *)
(* them. This is used to get completed numbers straight again and to reorder the entire numbers list at the end, too. *)
fun reorder([]) = []
	| reorder(x::xs) = reorder xs @ [x];

(* Converts char option to char. Useful because TextIO.input1 returns a char option. *)
fun charconvert(NONE) = #" "
	| charconvert(SOME x) = x;

(* Accepts the current character in the text file. *)
fun isDigit(x) = if ((ord(x) >= 48 andalso ord(x) <= 57) orelse (ord(x) = 126))
	(* If the character is a digit [having an ASCII code between 48 and 57], or is the negative sign ~, *)
	then true (* Return true. *)
	else false; (* Otherwise, return false. *)

(* Reads through the txt file given to it. *)
fun pread (file, x, chars, nums) =
	if TextIO.endOfStream(file) = false (* If not at the end of the file, *)
		then if (isDigit(x) = true) then pread(file, charconvert(TextIO.input1(file)), x::chars, nums) else pread(file, charconvert(TextIO.input1(file)), [], (doit((pcombine(reorder(chars))), nums))) (* Evaluate whether the current character is a digit or not with the evaluate function. *)
	else reorder(nums); (* If at the end of the file, reorder and return the list of numbers *)

(* Evaluate what to do if the current character is a digit. *)
(* If it is, call the pread file again, passing along the file, the next character, the current character stored in a list, and any numbers obtained so far. *)
(*fun evaluate(true, file, x, chars, nums) = *)
	(* If it is not a digit, call pread, passing along the file, the next character, an empty list, and then consume any characters stored, reordering them *)
	(* from front to back to back to front, imploding them into a string, and then converting from int option to int, before storing them in the nums list. *)
	(* If no characters are stored, returns empty list []. *)
	(*| evaluate(false, file, x, chars, nums) = ;*)

(* Main Function *)
(* Opens file name inputted into the function in the command line and passes it, the first character, and two empty lists to the pread function. *)
fun parse "" = []
	| parse file = pread(TextIO.openIn(file), charconvert(TextIO.input1(TextIO.openIn(file))), [], []);