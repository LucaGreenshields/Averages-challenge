def user_input():
    input_list = input("Enter a list elements separated by space ")
    string_list = input_list.split()
    num_list = [ float(item) for item in string_list ]
    return(num_list)   


def average(nlist):
    n = len(nlist)
    sum_n = sum(nlist)
    average = sum_n / n
    return(average)
print(f"average is {average(num_list)}")


def median(n_list):
    n = len(num_list)
    n_sort = num_list.sort()

    if n % 2 == 0:
        median1 = num_list[n//2]
        median2 = num_list[n//2-1]
        median = (median1 + median2)/2
    else:
        median = num_list[n//2]    
    return(median)

#num_list = [1, 4, 2, 5, 3]
print(f"median is {median(num_list)}")







#num_list = user_input()
#print(f"average is {average(num_list)}")


