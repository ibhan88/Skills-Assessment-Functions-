# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%

def total_cost(state_abbrev, item_cost, tax=0.05):
    """ To calculate the total cost of an item, tax included.

    This function will return the total cost of an item, including
    the tax. The default tax value is 5%, and for the state of
    California, the function will calculate the tax amount as 7%.

    For example::

        >>> total_cost("NY", 7.89)
        '$8.28'

        >>> total_cost("ca", 11.00)
        '$11.77'
    """

    state_abbrev = state_abbrev.upper()

    if state_abbrev == "CA":
        tax = 0.07
        total_amount_CA = item_cost + (item_cost * tax)
        rounded_amount_CA = round(total_amount_CA, 2)
        return "${:.2f}".format(rounded_amount_CA)
    else:
        total_amount = item_cost + (item_cost * tax)
        rounded_amount = round(total_amount, 2)
        return "${:.2f}".format(rounded_amount)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit_name):
    """ To check if a fruit is a "strawberry", "cherry", or "blackberry".

    The function checks if the input fruit is a "strawberry", "cherry",
    or "blackberry". If it is, it returns "True". If not, it will return
    "False".

    For example::

        >>> is_berry("watermelon")
        False

        >>> is_berry("cherry")
        True
    """

    fruit_name = fruit_name.lower()
    berry_list = ['strawberry', 'cherry', 'blackberry']
    if fruit_name in berry_list:
        return True
    else:
        return False


def shipping_cost(fruit_name):
    """ To check the shipping cost of a fruit.

    The function will return the shipping cost amount for a fruit.

    For example:

        >>> shipping_cost("grapefruit")
        '$5.00'

        >>> shipping_cost("strawberry")
        '$0.00'
    """

    if is_berry(fruit_name) == True:
        return "$0.00"

    elif is_berry(fruit_name) == False:
        return "$5.00"

    else:
        return None



# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.

def is_hometown(town_name):
    """ To determine if the string town_name matches "San Diego".

    If the town name is "San Diego", the function will return "True".
    If they do not match, it will return "False."

    For example::

        >>> is_hometown("san diego")
        True

        >>> is_hometown("CHICAGO")
        False
    """

    town_name = town_name.title()
    if town_name == "San Diego":
        return True
    else:
        return False


def full_name(first_name, last_name):
    """ To print the first and last names as a single string, titled.

    The function will concatenate the first and last names, then title
    it so that only the first letter of each word will be capitalized,
    which will then be returned.

    For example::

        >>> full_name("jane", "doe")
        'Jane Doe'
    """

    first_last_name = first_name + " " + last_name
    return first_last_name.title()


def hometown_greeting(town_name, first_name, last_name):
    """ To print a greeting (including a full name) dependent upon his/her hometown.

    The function will call the 'is_hometown(town_name)' function and
    depending on whether that function returns "True" or "False", a
    message will be printed.

    For example::

        >>> hometown_greeting("san francisco", "john", "doe")
        Hi, John Doe, where are you from?

        >>> hometown_greeting("san diego", "jane", "doe")
        Hi, Jane Doe, we're from the same place!
    """

    name = full_name(first_name, last_name)

    if is_hometown(town_name) == True:
        print "Hi, " + name + ", we're from the same place!"
    elif is_hometown(town_name) == False:
        print "Hi, " + name + ", where are you from?"
    else:
        return


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x=1):
    """ To increment some number by an integer, x.

    The function will return a new integer that is equal to the value of
    'x' plus 'y'.
    """

    def add(y):
        """ To determine what integer to increment by the x value."""
        return x + y

    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
addfive(5)
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def numbers_list(list_of_numbers, number):
    """ To append a number to a list of numbers.

    The function will add a number to the end of a list of numbers.

    For example::

        >>> numbers_list([0,5,7,98], 100)
        [0, 5, 7, 98, 100]
    """

    list_of_numbers.append(number)
    return list_of_numbers

#####################################################################
# To test all functions

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
