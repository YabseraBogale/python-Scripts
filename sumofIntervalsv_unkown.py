def sum_of_intervals(intervals):
    arr=intervals
    lst=set()
    for i in arr:
        j=i[0]
        while j<i[1]:
            lst.add(j)
            j+=1
    return len(lst)

arr=[
   [1, 2],
   [6, 10],
   [11, 15]
]
# for small numbers
print(sum_of_intervals(arr))
