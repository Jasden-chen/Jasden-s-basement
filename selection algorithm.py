from random import randint
from time import sleep

num_list = [randint(0,100) for i in range(100)]
num_list = list(dict.fromkeys(num_list))
print(num_list)
sorted_checker = num_list
counter = 0


def finding_smallest(the_list):
    global counter
    print('------------------------------')
    print('preparing to sort list....')
    sleep(2)
    while True:
        smallest = the_list[counter]
        for i in the_list[counter: len(the_list)]:
            if i <= smallest:
                smallest = i
        index_smallest = num_list.index(smallest)
        popped_element = num_list.pop(index_smallest)
        num_list.insert(counter, popped_element)
        sleep(0.2)
        print(num_list)
        if counter != len(num_list) - 1:
            counter += 1
        else:
            break


def check_results():
    sorted_checker.sort()
    if sorted_checker == num_list:
        print('Test passed')
    else:
        print('Test failed')


finding_smallest(num_list)
check_results()
