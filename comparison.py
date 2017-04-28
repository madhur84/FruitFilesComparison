""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""


def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    fruit_file = open(filename)
    fruit_file_read = fruit_file.read()
    fruit_file_read_list = fruit_file_read.split("\n")
    for fruit_item in fruit_file_read_list:
        print fruit_item
    fruit_file.close()
    return fruit_file_read_list


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.
    # list3 = []
    # for fruit_item_1 in lst1:
    #     for fruit_item_2 in lst2:
    #         if fruit_item_2 == fruit_item_1:
    #             list3.append(fruit_item_2)
    # return list3

    common_fruits = []
    for fruit in lst1:
        if fruit in lst2:
            common_fruits.append(fruit)

    return common_fruits

# Call your functions all the way at the bottom, after they've been defined.

var1= open_and_read_file("fruits_1.txt")
var2= open_and_read_file("fruits_2.txt")

cmp_fruits=compare(var1,var2)
print cmp_fruits