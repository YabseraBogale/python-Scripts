"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""
def order(sentence):
  # code here
    word=sentence
    lst=word.split(" ")
    wordorder={}
    for i in lst:
        for j in i:
            if j.isdigit():
               wordorder[int(j)]=i 
    ord=sorted(list(wordorder.keys()))
    answer=""
    i=0
    while i<len(ord):
        if(i!=len(ord)-1):
            answer+=wordorder[ord[i]]+" "
        else:
            answer+=wordorder[ord[i]]
        i+=1
            
    return answer
print(order("is2 Thi1s T4est 3a"))
