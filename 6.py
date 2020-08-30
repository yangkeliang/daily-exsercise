a=[1,2,3,4]
count=0
for i in a:  
    for j in a:       
        for k in a:
            if i!=j and j!=k and k!=i:
                print(i,j,k)
                count=count+1
print(count,"个数")
