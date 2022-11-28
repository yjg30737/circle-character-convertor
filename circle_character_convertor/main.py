import re

# currently numbers only
# convert circle characters into ordinary characters
# print the result
def convert_circle_into_ord(circle_characters):
    circle_characters_lst = re.split('\s|,', circle_characters)

    circle_characters_lst = list(filter(None, circle_characters_lst))

    first_number = 9312

    circle_characters_ord_lst = list(map(lambda x: ord(x)-first_number+1, circle_characters_lst))

    for i in circle_characters_ord_lst:
        print(i)