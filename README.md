# AddingCommas
In this problem, we want to insert commas in a piece of text by applying a set of custom rules that sprinkles commas in a sentence with no ambiguity and little simplicity. The idea is to develop an algorthm based on graph search to automate the rules.

Our rules for adding commas to an existing piece of text are as follows:

If a word anywhere in the text is preceded by a comma, find all occurrences of that word in the text, and put a comma before each of those occurrences, except in the case where such an occurrence is the first word of a sentence or already preceded by a comma.

If a word anywhere in the text is succeeded by a comma, find all occurrences of that word in the text, and put a comma after each of those occurrences, except in the case where such an occurrence is the last word of a sentence or already succeeded by a comma.

Apply the preceding two rules repeatedly until no new commas can be added using either of them.

As an example, consider the text
  please sit spot. sit spot, sit. spot here now here.
Because there is a comma after spot in the second sentence, a comma should be added after spot in the third sentence as well (but not the first sentence, since it is the last word of that sentence). Also, because there is a comma before the word sit in the second sentence, one should be added before that word in the first sentence (but no comma is added before the word sit beginning the second sentence because it is the first word of that sentence). Finally, notice that once a comma is added after spot in the third sentence, there exists a comma before the first occurrence of the word here. Therefore, a comma is also added before the other occurrence of the word here. There are no more commas to be added so the final result is
  please, sit spot. sit spot, sit. spot, here now, here.

Sample Output 1
For the input line:
  please sit spot. sit spot, sit. spot here now here.
we should produce the output
  please, sit spot. sit spot, sit. spot, here now, here.

Sample Output 2
For the input line:
  one, two. one tree. four tree. four four. five four. six five.
we should produce the output
  one, two. one, tree. four, tree. four, four. five, four. six five.
