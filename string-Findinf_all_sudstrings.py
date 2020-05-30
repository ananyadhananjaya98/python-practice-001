def substring(string,sub):
    len1 = len(string)
    list1=[]
    for i in range(len1):
        for j in range(i,len1+1):
            list1.append(string[i:j])
    print(list1)
    count=0
    for i in list1:
        if sub == i:
            count+=1
    print(count)


substring("ABCDCDC","CDC")
