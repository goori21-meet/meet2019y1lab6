def add_numbers(num_list):
    num_list2=0

    for num in num_list:

        print(num)
        num_list2=num_list2+num
    return num_list2


    
    
    



answer = add_numbers(range(1,10+1))
print(answer)
