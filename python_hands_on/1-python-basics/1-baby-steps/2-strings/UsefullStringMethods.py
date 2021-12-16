# Make a variable to play around with:

course = 'Python programming'

# Lets make it all caps:

course_all_upper = course.upper()  # Java course_all_upper =course.toUpperCase()
print(course_all_upper)

# Convert to lower case:

course_all_lower = course_all_upper.lower()  # Java course_all_lower =course.toLowerCase()
print(course_all_lower)

# Create 2 variables all lowercase:

first_name = 'alexander'
last_name = 'keisse'

# First char of every word will be uppercase:

full_name = F'{first_name} {last_name}'.title()
print(full_name)
''' 
Java: No such thing, 
we could use for loop and split to achieve the result
'''

# Let's see how we strip excessive white spaces:

course_excess_whitespace = '           course'
print(course_excess_whitespace)

# Good practice to do this with user input:

course_fixed = course.strip()
print(course_fixed)

# You can even take it a step further trimming left or right:

course_excess_whitespace_left = '           course'
course_excess_whitespace_right = 'course         '

# Left trim:

course_fixed_left = course_excess_whitespace_left.lstrip()
# Java: System.out.println(name_excessive_whitespace_trail.stripLeading());

# Right trim:

course_fixed_right = course_excess_whitespace_right.rstrip()
# Java: System.out.println(name_excessive_whitespace.stripTrailing());

# Print the results:

print(course_fixed_left)
print(course_fixed_right)

# If you want to search a string value for a certain value:

print(course.find('pro'))  # You will find start index
# Java: System.out.println(name.indexOf('h'));


# If the value can't be found -1 is returned:

print(course.find('Pro'))
# Java: System.out.println(name.indexOf('a'));

# Lets replace a char in our string course for another one:

course_replaced_a_char = course.replace('o', '0')
print(course_replaced_a_char)
# Java: System.out.println(name.replace('h', 'b'));

# Lets see if a certain value is present in our course variable:

print('Python' in course)

# Or see if it is absent:

print('python' not in course)
