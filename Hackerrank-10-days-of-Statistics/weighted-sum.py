# Weighted sum of two list

n = int(input())
x = list(map(int, input().split())) 
w = list(map(int, input().split()))

z = 0
for i in range(0,n):
    z = z + x[i] * w[i]
weig_sum = z/sum(w)
print(round(weig_sum,1))
