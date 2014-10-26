import itertools

length = int(input())
l = list(map(int,raw_input().split()))

found = 0
count = -1

for j in range(length , 1, -1):
		for i in itertools.combinations(l,j):
			if sum(i) >= 0: 
				found = 1
				count += 1
#				print(i, end="")
		if found == 1: break
		
if count > 0 : print j, count
else : print count