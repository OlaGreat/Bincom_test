def sort_a_list(list):
    for i in range(len(list)):
        print(i)
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
  
num = [9,4,6,8,1,2,3]
print(sort_a_list(num))