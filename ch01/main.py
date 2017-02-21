import sys

def func_1_1(str):
    """
    check for unique chars
    """
    if(len(str)==0):
        return False
    
    ht = {}

    for c in str:
        if c not in ht:
            ht[c] = 1
        else:
            return False
    return True
    
def call_func_1_1():
    while(True):
        str = raw_input("Please input a string:\n")
        result = func_1_1(str)
        print(result)
        print("\n")
        


def main():
    call_func_1_1()

if __name__ == "__main__":
    main()
