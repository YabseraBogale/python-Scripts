"""
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

"""


def str_join(lst):
    str=""
    for i in lst:
        str+=i
    return str


def spin_words(sentence):
    # Your code goes here
    lst=sentence.split(" ")
    str=""
    for i in lst:
        if len(i)>=5:
            j=list(i)
            j.reverse()
            j=str_join(j)
            str+=j+" "
        else:
            str+=i+" "
    
    return str.rstrip()

print(spin_words("word"))
print(spin_words("Single word"))