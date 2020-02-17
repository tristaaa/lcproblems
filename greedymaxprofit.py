n,m=list(map(int,input().split()))
engine,task=[],[]
for i in range(n):
    engine.append(tuple(map(int,input().split())))
for i in range(m):
    task.append(tuple(map(int,input().split())))
    
#first sort by time, then by task rank
engine.sort(key=lambda x:(x[0],x[1]),reverse=True)
task.sort(key=lambda x:(x[0],x[1]),reverse=True)

profit=0
count=0
cnt=[0]*101
j=0
for i in range(m):
    while j<n and engine[j][0]>=task[i][0]:
        cnt[engine[j][1]] += 1
        j += 1
    for k in range(task[i][1],101):
        if cnt[k]:
            count += 1
            cnt[k] -= 1
            profit += 200 * task[i][0] + 3 * task[i][1]
            break
print(count,profit)
