def print_formatted(number):
    m=len(bin(n).replace("0b", ""))
    # your code goes here
    for i in range (1,n+1):
        print  str(i).rjust(m) , str(oct(i)[1
        :]).rjust(m).upper(), hex(i).replace('0x',"").rjust(m).upper() , str(bin(i).replace("0b", "").rjust(m))
    return


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
