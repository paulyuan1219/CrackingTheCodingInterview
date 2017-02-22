# Bloomberg

## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.


# vector of integers
# there is at least one duplicate in the array
# write a function to return such a duplicate

# [1, 0, 0, 2] --> 0
# [1, 1, -10, -10] --> 1 or -10


def func_findduplicate(A):
    # input: A is a list of ints
    # output: the value of the duplicate, or null
    ht={}
    for element in A:
        if element in ht:
            return element
        else:
            ht[element] = 1
    return Null
    
# Now suppose the list has length N
# and all elements are between 1 and N-1
# How does this change your two approaches: hash table and sorting?

# [1, 2, 3, 1] --> 1
# [1, 3, 3, 1] --> 1 or 3


# Additionally...
# The array is very large and exists in a file on disk
# It can't fit entirely in memory
# The file is read only
# What can we do?


Q. We are doing sentiment detection for tweets, for each company name and the judge depends on the stockholders. What will you do?

