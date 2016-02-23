__author__ = 'meldd'
# melanie desantis

# project 2- write a program to ask user how many levels the pyramid should have, the character with which to build
# output teh complete symmetrical pyramid

def pyramidsymm():  # define the function
    levels = int(input("enter how many levels you want to build"))  # ask the user for the integer of levels
    block = (input("enter which character you want to use to build your pyramid"))  # ask what character to use

    print(levels)  # check the number of levels
    print('huzzah, a pyramid of ', block, )  # check the character

    space = " "  # set the space as a variable to use and repeat
    q=1  # set q variable as anything

    for i in range(levels+1, 1, -1):  # for i in the range input level to one, moving by a step of neg 1
        spacenum = (space * i)  # the number of spaces is the number of levels moving down by neg 1 step
        #print ('x', spacenum, 'x')  to check

        print (spacenum, block*q,) # print hte spaces and the blocks
        q=q+2  # so the q increases as we add levels until we reach limit

pyramidsymm()  # run the function
