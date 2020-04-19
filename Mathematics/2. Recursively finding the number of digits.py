def find_digits(number):
    if(number==0):
        return 0
    return 1 + find_digits(number//10)

if(__name__=="__main__"):
    print(find_digits(int(input())))