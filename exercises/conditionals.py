# sum=0
# i=0
# while sum<=10000 :
# 	if(i%2==0):
# 		sum=sum+i
# 	i+=1

# print(i-1)

def is_prime(x):
	i=2
	while i<x:
		if(x%i==0):
			return "not prime"
		else:
			i+=1
	return"prime"

print(is_prime(5191))
 




