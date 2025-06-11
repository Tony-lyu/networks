def cal(first, last, size):
    unit = ["万", "亿", "万亿"]
    num = int((first + last) * size / 2)
    if num >= 1000000000000: 
        return f"{int(num/1000000000000)}{unit[2]}"
    elif num >= 100000000:
        return f"{int(num/100000000)}{unit[1]}"
    elif num >= 10000:
        return f"{int(num/10000)}{unit[0]}"
    return f"{int((first + last) * size / 2)}"

def exp(first, last):
    sum = 0
    for i in range(first - 1, last):
        sum += (i%10 + 1)
    return sum
def total():
    s = 0
    for i in range(1, 101):
        s += equation(i)
    return s
def equation(x):
    return 0.00001 * pow(x, 5) + 0.00301 * pow(x, 4) - 0.18655 * pow(x, 3) + 5.24157 * pow(x, 2) - 38.84663 * x + 86.54224
print(exp(1, 500)/ (total()/10000))
print()