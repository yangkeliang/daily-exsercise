with open("感想.txt","r",encoding="utf-8") as f:
    j=1
    for i in f:
        filenameA="A_"+str(j)+".txt"
        filenameB="B_"+str(j)+".txt"
        if i == "\n":
            j+=1
        if "A:" in i:
            with open(filenameA,"a",encoding="utf-8") as f:
                f.write(i)
        if "B:" in i:
            with open(filenameB,"a",encoding="utf-8") as f:
                f.write(i)