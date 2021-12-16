# In terms of typing, programming languages fall into 2 categories:

# 1. Static typing; C++, C#, Java
# 2. Dynamic typing; JavaScript, Ruby, Python

# In a static language you would define a variable as so:
# int studentCount = 1;
# A programming language is statically typed if the type of a variable is known at compile time.

# Once you declared the variable as of type int you can only use it to store int values,
# so the following piece of code would give a compilation error:

# studentCount = true;

# When using a dynamic language the type will be determined at runtime,
# and because of this mechanism a variable can change type.
# runtime (the period of time when a program is running and generally occurs after compile time)
# Difference between the runtime and the compile time https://www.baeldung.com/cs/runtime-vs-compile-time

# This is how to find out the type of a variable:

student_count = 1
print(type(student_count))

# Returns a type object

print(type(type(1)))

# Java: Integer number = Integer.valueOf("10"); cannot do int number =10 and getClass etc
# System.out.println(number.getClass().getName());

# Some examples of types in Python:

print(type(1.1))  # Java: Float number = Float.valueOf("1.1"); #wrapper class conversion
print(type(True))  # Java: Boolean number = Boolean.valueOf("true"); #wrapper class conversion
print(type(''))  # Java: String student ="";

# What if we change the type of value we store in student_count to a boolean:

student_count = True  # Java: Boolean student_count = Boolean.valueOf('true');
print(type(student_count))  # Lets print again and check the result
