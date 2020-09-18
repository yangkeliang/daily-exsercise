def isip(ip):
    s=0#计数用
    ip=str(ip)#为使用split强制转化为字符串
    list1=ip.split(".")#分割
    if len(list1) != 4:#判断是否为4段
        print("请输入正确的格式")
    else:
        try:#输入非数字报错处理
            for i in list1:
                int(i)#触发一个错误，确认为整型 
            for i in range(4):
                if i == 0:    
                    if int(list1[i]) >0 and int(list1[i]) <= 255:#判断第一个数是否为0-255
                        s = s+1#计数        
                else:
                    if int(list1[i]) >= 0 and int(list1[i]) <= 255:
                        s = s+1#计数 
        except Exception as e:
            print("异常为{}".format(e))
    if s == 4:
        return True
    else:
        return False
        
if __name__=="__main__":
    print(isip(input("请输入字符串：")))
