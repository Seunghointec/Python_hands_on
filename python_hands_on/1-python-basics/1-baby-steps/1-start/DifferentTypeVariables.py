# Integer:

students_count = 1000  # Java: int students_count=1000;
print(students_count)  # System.out.println(students_count);

# Floating number:

rating = 4.99  # Java: float rating=4.99;
print(rating)

# Boolean:

is_published = False  # Java: bool is_published=False;
print(is_published)

# String:

string_sq = "This is a literal string"  # Java: String sq= "This is a literal string";
print(string_sq)

string_dq = 'This is another string'  # Java: String cannot use single quotes, only char
print(string_dq)

multiple_line_string = """ 
Multiple
line
String
"""  # Java: No options of Multiple line String (optional) stringBuilder or StringJoin()
print(multiple_line_string)

# Different ways of initialising variables:

# First way:

x = 1
y = 2

print(x, y)

# Second way:

z, h = 1, 2  # Java: int z,h; but values in different lines
print(z, h)  # Java z=1; h=2; (never z=1, h=1; or z,h =1,2)

# Third way:

first_var = second_var = 1  # Java: int first_var, second_var;
print(first_var, second_var)  # Java: first_var=second_var=1

# Overview of literals possible in Python:

# 42                                Integer literal
# 3.14                              Floating point literal
# 'hello'                           String literal
# "world"                           Another String literal
# """Good                           Triple quoted string literal
# night"""

# Stuff that we will see later:

# [42, 3.14, 'hello']               List
# []                                Empty list
# 100, 200, 300                     Tuple
# ()                                Empty tuple
# {'x':42, 'y':3.14}                Dictionary
# {}                                Empty dictionary
# {1, 2, 4, 8, 'hello'}             Set
# There is no literal to denote an empty set; use the builtin function set() instead
