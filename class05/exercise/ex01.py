# Let's create a Product from different formats

# you are designing a product class
    # product class needs:
        # name
        # price
        # category

# the data to create this class may arrive in 3 different formats:
    # 1. separate constructor arguments (__init__)
    # 2. one comma-separated string
    # 3. a dictionary

# you need to design the class so all three formats can be used cleanly.

# example of the dictionary :
example_dict = {
    "name": "something",
    "price" : 0,
    "category": "something else"
}

# example of comma separated:
ex_str = "something,0,something else"
# hint --> int(str) converts a string to integer