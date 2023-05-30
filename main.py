# Create a function called 'kiss' with two arguments, a 'name' and an 'amount'. done
# Once called, it should print 'kiss name' n times for the amount that is given.


def kiss(name, amount):
    n = 0

    while n < amount:
        print('lex kiss', name)
        n = n + 1


kiss('anna', 10)
