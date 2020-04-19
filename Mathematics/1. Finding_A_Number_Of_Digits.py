def find_digits(number):
    count=0
    while number != 0:
        count += 1
        number=number//10
    return count
if __name__=="__main__":
    print(find_digits(int(input())))
