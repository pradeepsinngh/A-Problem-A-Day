# find std. deviation

n = int(input())
y = list(map(int, input().split()))

mean = sum(y)/n
variance = sum([((x-mean) ** 2) for x in y]) /n
stddev = variance ** 0.5
print(round(stddev,1))
