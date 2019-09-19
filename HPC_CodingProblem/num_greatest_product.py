from functools import reduce
import argparse


def num_greatest_product(nums, digit):
    """
    :param nums: 1000 digit number
    :param digit: an integer less than 1000
    :return: a list with eight adjacent digit with greatest product and an integer with this greatest product
    """
    # Convert each eight adjacent digit number into a list of integers
    digits = len(nums)
    max_product = 0
    num_max_product = []
    k = 0
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
    return 'The {} adjacent digits which have the greatest product are {}' \
           ' and the greatest product is {}'.format(digit, num_max_product, max_product)


def main():
    parser = argparse.ArgumentParser(description="Find the adjacent digits in the 1000 digit number")
    parser.add_argument('-number', metavar='', help="1000 digit number", type=str, required=True)
    parser.add_argument('-digit', metavar='', help="Adjacent digit",  type=int, required=True)
    args = parser.parse_args()
    print(num_greatest_product(args.number, args.digit))


if __name__ == '__main__':
    main()

nums = '3766581235885941622054540050228447514162777869412307699482907769113268717216818322831603491835999456015306915009196661427591452909871214219792485776087253286386945942663949956280302377388971714236415605168862773550156548824873689737766284562457836197902674997734737908387650371844408009421100914050765521827781655182806129058522352838472989652688571683680665438395803243794489830567998343203397981373552644309879795957322883020671901669290704497751685870539575543632177623725028726840870016429503564354896057020404025619555440159796686935523081354355119387766201895202371147907112778884969266539280935452003712638970422340890791962244529017494651550289995762505866212386393472458374741386036991340760970327022447106502711257671708182087831698677130077927731626466195021513131952322762659409302452718743061757527857578831917621650745174966732316231446870605534431568974878576006012026939455247174486040603096495646182217557200423380237313587369836078574982810508277521659834594761360129982400036745363'

#print(num_greatest_product(nums, 6))





