#in Python, a .py file is called a module
#want to make use of the printPattern function which is in another file.

# import funcdemo #going to reference the funcdemo module

# funcdemo.printPattern('*', 2, 5)
# funcdemo.dummy()

# import math  #math.py
# print( math.sqrt(4) )

# from funcdemo import printPattern #specically going to use printPattern

# printPattern('^', 2, 10)

# from funcdemo import * #going to use all the functions in the module
# printPattern('$', 2, 10)
# dummy()

# import random 
# #from random import randrange
# print( random.randrange(1, 11))

import funcdemo 

#no code