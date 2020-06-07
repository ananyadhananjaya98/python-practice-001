def merge_the_tools(string, k):
    new_list = []
    for i in range(0,len(string),k):
        j = i+(k)
        new_list.append(string[i:j])
    final_list=[]
    for i in new_list:
        list02 = []
        for j in i:
            if j not in list02:
                list02.append(j)
        final_list.append(''.join(list02))
    for i in final_list:
        print(i)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string,k)
