from math import pi

#1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

#2
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#3
first_name = 'Seungho'
last_name = 'Kang'

full_name = f'{first_name} {last_name}' [::-1]
print(full_name)

#4

my_list = ['3','5','7','23']
my_tuple = ('3','5','7','23')

print(my_list)
print(my_tuple)

#5
print("Please enter your file name")
file_name =input()
file_name_extension =file_name.split('.')
print('Your extension is: ' + repr(file_name_extension))


#6
colour_list = ["Red","Green","White" ,"Black"]
print(colour_list[0,3])