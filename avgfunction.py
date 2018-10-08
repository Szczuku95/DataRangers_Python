#zakładam, że nie można korzystać z niczego poza pętlami i podstawowymi operatorami :P

def avg(input):
    sum = 0
    length = 0
    for number in input:
        sum += number
        length += 1
    return sum/length



print(avg([2,2,2,2,2,2]) - 2 < 0.0000001)
print(avg([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(avg([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)

