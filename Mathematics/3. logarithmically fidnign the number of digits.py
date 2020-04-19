import math
def find_digits(number):
    return int(math.log(number,10)+1)

if __name__=="__main__":
    print(find_digits(int(input())))