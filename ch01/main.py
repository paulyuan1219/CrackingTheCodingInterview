import sys

def func_2_1(str1, str2):
    s1 = str1.sort()
    s2 = str2.sort()
    
    if s1==s2:
        return True
    else:
        return False
def call_func_2_1():
    while(True):
        str = raw_input("Please input 2 strings:(No space allowed within one string)\n")
        fields = str.split()
        
        result = func_2_1(fields[0], fields[1])
        print(result)
        print("\n")

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
        
def func_1_2(str):
    """
    check for unique chars
    """
    if(len(str)==0):
        return False
    
    for i in range(len(str)-1):
        for j in range(i+1, len(str)):
            if(str[i] == str[j]): return False
    return True
                       
def call_func_1_2():
    while(True):
        str = raw_input("Please input a string:\n")
        result = func_1_2(str)
        print(result)
        print("\n")

                       

def main():
    call_func_2_1()

if __name__ == "__main__":
    main()
