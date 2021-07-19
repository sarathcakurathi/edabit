"""
Look-And-Say Sequence
The look-and-say sequence is generated by describing each group of identical digits in the previous term. If we start at "1", the first five terms in the sequence are:

"1" = "one 1" = "11"
"11" = "two 1's" = "21"
"21" = "one 2, one 1" = "1211"
"1211" = "one 1, one 2, two 1's" = "111221"
"111221" = "three 1's, two 2's, one 1" = "312211"
Given a term (as a string), return the next term in the sequence.

Examples
look_and_say("1211") ➞ "111221"

look_and_say("111221") ➞ "312211"

look_and_say("31131211131221") ➞ "13211311123113112211"
Notes
Terms will only include the digits 1, 2, and 3."""

def look_and_say(term):
    pass