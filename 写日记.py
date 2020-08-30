from time import strftime, localtime
with open("E:\日记.txt","a") as f:
    text=input("say something:")
    f.write(strftime('%Y-%m-%d %H:%M:%S',localtime())+"\n")
    f.write(text+"\n")
    f.write('--------------------------------------------------'+'\n')