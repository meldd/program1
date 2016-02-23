__author__ = 'meldd'

#project 1 : ask the user how many levels the pyramid should have
# the building block character to suse for the pyramid and then output the right half of the pyramid

def HalfPyramid():

  blocknum = int(input("enter how many levels you want to build"))  # ask the user for the integer of levels
  block = (input("enter which character you want to use to build your pyramid"))  # ask what character to use

  print (blocknum)  # check the number of letters
  print ('huzzah, a pyramid of ', block,) # check the character

  for levels in range(1, blocknum+1):  # for the range of the levels (necessary to add one as not inclusive)
    print(block * levels)  # print the character that number of times, using variables usually ( ' ! ' * 5 )
    # print(levels) # to check its printing the right levels


HalfPyramid()
