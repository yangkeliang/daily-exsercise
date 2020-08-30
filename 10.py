import time
dic={
    "red":30,
    "green":35,
    "yellow":3
}
for i in dic:
    for j in range(dic[i],-1,-1):
        print(i,"灯还有",j,'秒')
        time.sleep(1)
    print("\n")