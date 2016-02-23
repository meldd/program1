__author__ = 'meldd'
# melanie desantis

# y = (x**2) / 4  # exponents = **
# ASK USER FOR A RANGE OF VALUES FOR X, A SCALING FACTOR FOR PARABOLA, AND OUTPUT PARABOLA WIH RIGHT SIDE UP


xmin= int(input("enter the min of the range for x in your parabola"))  # prompt user for min and max of x
xmax = int(input("enter the max range of x"))
#xmin = -15  hardcoding to test
#xmax = 15  hardcoding to test
print ("(",xmin,",",xmax,")")  # print the min and max values

space=' '  # set space
y =1
spaceneg=1


for i in range(xmax,xmin, (-1)):  # move down in steps by neg 1

    for i in range (0, i, 1):
         if i != i%2: # if the value of i is not even

            print ("  ",)

    if 0 == i % 2 and i >= 0: # to illustrate curve skips lines between plot points
            spacenum=(i*space)  # to get the spaces inside the parabola,
            #  variable is doubled in print statement as it corrseponds to only half of function
            spaces=spaceneg*space  # to get the number of spaces preceding the parabola
            y= ((i**2)/4)         # y=((i**2)/4)  the function of the parabola

            print(spaces, '*', spacenum,spacenum,'*')  # print the spaces, the star in the position of the y values

            spaceneg = (spaceneg+2)  # space neg refers to



#print('.',spacenum,'.')
          #      print(spaces,y, '*', spacenum,'.',spacenum,'*', y)    remove first y to check for symmetry

'''
  print ("(",xmin,",",xmax,")")

space=' '

y =1
for i in range(xmin+1, xmax+1, (1%4)):
    spacenum=i*space
    y= i**2
    print(spacenum,y)

space = " "
#    spaceamt= [1, levels]
q=1
block = "*"

for i in range(xmin, xmax, (1%4)):
    spacenum = (space * i)
    #print ('x', spacenum, 'x')

    print (block*q, spacenum, block*q)
    q=((q**2)%4)
'''

'''
limit = int(input ('how many x values do you have?'))
x = [int(input('enter one of the values for x for which you want to calculate the parabola.' )) for x in range(0 ,limit) ]
print (x)

y = (x**2)%4
print (y)
'''