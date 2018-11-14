from math import pow

def num_sys_conv(num_sys):
    lst = num_sys.split()
    num = int(lst[0])
    sys = int(lst[1])
    return_num = ""
    while num > 0:
        if sys == 2:
            x = []
            sum_dec = 0
            for char in str(num):
                x.append(char)
            x = x[::-1]
            for elem in range(len(x)):
                sum_dec += int(x[elem]) * pow(2, int(elem))
            return_num = ("| 10", (str(sum_dec)))
            return return_num[::-1]
        if sys == 10:
            x = num % 2
            return_num += str(x)
            num = int(num / 2)
    return (return_num[::-1], "| 2")


def main():
    num_sys = input("Type in a number, and its number system (2 or 10): ")
    length = len(str(num_sys_conv(num_sys))) - 6
    print("/", "-" * length, "\\")
    print("| ", *num_sys_conv(num_sys), "|")
    print("\\", "-" * length, "/")


if __name__ == '__main__':
    main()