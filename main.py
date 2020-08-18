def user_input():
    input_list = input("Enter a list elements separated by space ")
    string_list = input_list.split()
    num_list = [ float(item) for item in string_list ]
    return(num_list)   


def average(n_list):
    n = len(n_list)
    sum_n = sum(n_list)
    average = sum_n / n
    return(average)



def median(n_list):
    n = len(n_list)
    n_sort = n_list.sort()

    if n % 2 == 0:
        median1 = n_list[n//2]
        median2 = n_list[n//2-1]
        median = (median1 + median2)/2
    else:
        median = n_list[n//2]    
    return(median)


def mode(n_list):
    freq_dict = {}
    for num in n_list:
        freq_dict[num] = freq_dict.setdefault(num, 0) + 1
    freq_list = [ (key, value) for key, value in freq_dict.items()]
    sorted_freq_list = sorted(freq_list, key=lambda item: item[1], reverse=True) 
    max_freq = sorted_freq_list[0][1]
    result = [ item[0] for item in sorted_freq_list if item[1] == max_freq]
    return(result)

num_list = user_input()
print(f"average is {average(num_list)}")
print(f"median is {median(num_list)}")
print(f"mode is {mode(num_list)}")


