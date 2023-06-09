# Text taken from Madtakes.com
# Url: https://www.madtakes.com/libs/172.html
# Title: The walmart difference ad-lib
# Contributed by tony

print("Please choose the required words:")

first = input("Verb: ").upper()
second = input("Adjective: ").upper() 
third = input("Noun (plural): ").upper()
fourth = input("Adjective: ").upper()
fifth = input("Verb ending in ""ing"": ").upper()
sixth = input("Verb: ").upper()
seventh = input("Number: ").upper()
eighth = input("Adjective: ").upper()
ninth = input("Noun (plural): ").upper()
tenth = input("Noun (plural): ").upper()
eleventh = input("Noun (plural): ").upper()
twelfth = input("Relative (plural): ").upper()
thirteenth = input("Adjective: ").upper()
fourteenth = input("Adjective: ").upper()
fifteenth = input("Noun (plural): ").upper()

my_string = '''Come {} at Walmart, where you'll receive {} discounts on all of your favorite brand name {}. Our {} and {} associates are there to {} you {} hours a day. Here you will find {} prices on the {} you need. {} for the moms, {} for the kids and all the latest electronics for the {}. So come on down to your {} {} Walmart where the {} come first. '''.format(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth. fifteenth)
print(my_string)