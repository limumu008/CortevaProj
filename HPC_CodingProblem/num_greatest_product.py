from functools import reduce

import argparse


def num_greatest_product(nums, digit):
    """
    Find the adjacent digit number in the 1000-digit number which have the greatest product.
    :param nums: 1000 digit number
    :param digit: an integer less than 1000
    :return: a list with eight adjacent digit with greatest product and an integer with this greatest product
    """
    assert 0 < digit <= 1000 and type(digit) == int, 'Digit parameter must be an integer between 1 and 1000'
    digits = len(nums)
    assert digits == 1000, 'The input number must be a 1000-digit number'
    max_product = 0
    num_max_product = []
    k = 0
    # Convert each adjacent digit number into a list of integers
    num_digit = [int(d) for d in nums]
    while k < digits-digit:
        # Choose eight adjacent digit number as a list
        assigned_digits_num = num_digit[k:k+digit]
        # Once met zero, loop will start after zero number
        if 0 in assigned_digits_num:
            k = k + digit
            continue
        product = reduce(lambda x, y: x*y, assigned_digits_num)
        if product > max_product:
            max_product = product
            num_max_product = assigned_digits_num
        k += 1
    if max_product == 0:
        num_max_product = num_digit[:digit]
    return 'The {} adjacent digits which have the greatest product are {}' \
           ' and the greatest product is {}'.format(digit, num_max_product, max_product)

# def main():
#     parser = argparse.ArgumentParser(description="Find the adjacent digits in the 1000 digit number")
#     parser.add_argument('-number', metavar='', help="1000 digit number", type=str, required=True)
#     parser.add_argument('-digit', metavar='', help="Adjacent digit",  type=int, required=True)
#     args = parser.parse_args()
#     print(num_greatest_product(args.number, args.digit))


if __name__ == '__main__':
    # main()

    nums = '37665812358859416220545400502284475141627778694123' \
           '07699482907769113268717216818322831603491835999456' \
           '01530691500919666142759145290987121421979248577608' \
           '72532863869459426639499562803023773889717142364156' \
           '05168862773550156548824873689737766284562457836197' \
           '90267499773473790838765037184440800942110091405076' \
           '55218277816551828061290585223528384729896526885716' \
           '83680665438395803243794489830567998343203397981373' \
           '55264430987979595732288302067190166929070449775168' \
           '58705395755436321776237250287268408700164295035643' \
           '54896057020404025619555440159796686935523081354355' \
           '11938776620189520237114790711277888496926653928093' \
           '54520037126389704223408907919622445290174946515502' \
           '89995762505866212386393472458374741386036991340760' \
           '97032702244710650271125767170818208783169867713007' \
           '79277316264661950215131319523227626594093024527187' \
           '43061757527857578831917621650745174966732316231446' \
           '87060553443156897487857600601202693945524717448604' \
           '06030964956461822175572004233802373135873698360785' \
           '74982810508277521659834594761360129982400036745363'

    print(num_greatest_product(nums, 4))
    print(num_greatest_product(nums, 8))





