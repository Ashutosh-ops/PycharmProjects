def summation(joint):
    number = 0

    while joint > 0 or number > 9:

        if joint == 0:
            joint = number
            number = 0
        number += joint % 10
        joint /= 10

    return number


# Driver method
n = 1234
print(summation(n))
