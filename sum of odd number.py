"""
Given the triangle of consecutive odd numbers:
			1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

"""
def row_sum_odd_numbers(n):
    #your code here
    lst=[1]
    i=0
    while i<n:
        lst.append(2*i+lst[i])
        i+=1
    j=0
    sum=0
    lst2=[]
    number=lst[len(lst)-1]
    while j<n:
        lst2.append(number)
        sum+=number
        number+=2
        j+=1
    return sum
    
    
    
print(row_sum_odd_numbers(3))
