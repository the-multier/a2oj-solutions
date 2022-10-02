n = int(input())
nums = [int(x)//100 for x in input().split()]
if sum(nums)%2 == 1 or (min(nums)==2 and len(nums)%2!=0):
	print("NO")
else:
	print("YES")