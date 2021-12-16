# Let's make 2 String variables to play with:

first = 'Alexander'
last = 'Keisse'

# And concatenate them together:

full = first + ' ' + last
print(full)

# Better practice would be using an expression,
# which is evaluated at runtime:

full_name = f'{first} {last}'  # java: System.out.println(MessageFormat.format("my name is {0}", firstName +LastName));
full_name_also_valid = F"{first} {last}"

print(full_name)
print(full_name_also_valid)

# Get the full powaaah:
fancy_char_counting = F'{"Name has:"} {len(full_name) - 1} {"chars."}'  # Java:System.out.println
# (MessageFormat.format "Name has", (firstName +LastName).length() + "chars"));
print(fancy_char_counting)
