


def binarySearch(list  : [], number_to_search:int):
    list.sort()
    half_of_list = len(list) // 2
    index=0
    if list[half_of_list] == number_to_search:
        print(f"the number you are searching for is at index {half_of_list}")

    else:
        if number_to_search < list[half_of_list]:
            for i in list[0:half_of_list] :
                index+=1
                if i == number_to_search:
                    print(f"the number you are searching for is at index {index-1}")
                    break
                else:
                    if index == half_of_list:
                        print(f"the number you are searching for is not in the list")
        else:
            for i in list[half_of_list:len(list)]:
                half_of_list+=1
                if i == number_to_search:
                    print(f"the number you are searching for is at index {half_of_list-1}")
                    break
                else:
                    if index == half_of_list:
                        print(f"the number you are searching for is not in the list")


            

    

nm = [1,2,3,10,8,11,12,13,14,16,17]
print(binarySearch(nm, 8))

    
