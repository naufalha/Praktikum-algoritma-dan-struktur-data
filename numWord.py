# install the num2words library using pip
# uncomment the line below if you haven't installed it yet
# !pip install num2words

# import the num2words library
from num2words import num2words

# define an integer number
my_number = 123

# convert the number to its word representation
word_representation = num2words(my_number)

# print the result
print(word_representation) # output: "one hundred and twenty-three"
