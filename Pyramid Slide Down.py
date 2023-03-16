
def splitAndGive(index,array):
	lst=[]
	i=2
	lst.append(array[index])
	lst.append(array[index+1])
	
	if lst[0]>lst[1]:
		print(lst[0])
		return lst[0]
	print(lst[1])
	return lst[1]
	

def down(array):
	if len(array)==1:
		return array[0][0]
	py=array
	i=0
	num=py[i][i]
	sum=num
	i+=1
	while i<len(py):
		num=splitAndGive(py[i-1].index(num),py[i])
		sum+=num
		i+=1
	return sum

arr=[        	  [75],
		        [95, 64],
               [17, 47, 82],
              [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
           [19,  1, 23, 75,  3, 34],
	      [88,  2, 77, 73,  7, 63, 67],
	     [99, 65,  4, 28,  6, 16, 70, 92],
	   [41, 41, 26, 56, 83, 40, 80, 70, 33],
      [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
   [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
 [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ]
#print(down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))
print(down(arr))
