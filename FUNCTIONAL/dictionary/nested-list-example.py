#List example without nesting
def main1():
    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthName = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    for i, name in enumerate(monthName): 
        print('{} has {} days'.format(name, month[i]))

# List example with nesting
def main2():
    month = [['January', 31], ['February', 28], ['March', 31], ['April', 30], ['May', 31], ['June', 30], 
    ['July', 31], ['August', 31], ['September', 30], ['October', 31], ['November', 30], ['December', 31]]
    for m in month:
        print('{} has {} days'.format(m[0], m[1]))

main2()

# <list>.sort()
# Sort (order) the list. A comparison function may be passed as a parameter.

# <list>.reverse()
# Reverse the list.

# <list>.index(x)
# Returns index of first occurrence of x.

# <list>.count(x)
# Returns the number of occurrences of x in list.