# -*- coding: utf-8 -*-
__author__ = 'koef'


def bouquets(narcissus_price, tulip_price, rose_price, money):
    flowers = [narcissus_price, tulip_price, rose_price]
    flowers.sort()

    number_of_bouquets = 0
    for a in range(int(money/flowers[2])+1):
        if a*flowers[2] <= money:
            for b in range(int(money/flowers[1])+1):
                if (a*flowers[2] + b*flowers[1]) > money:
                    break
                if (a+b)%2 == 0:
                    for c in range(1, int(money/flowers[0])+1, 2):
                        if (a*flowers[2] + b*flowers[1] + c*flowers[0]) > money:
                            break
                        if (a+b+c) > 0 and (a*flowers[2]+b*flowers[1]+c*flowers[0]) <= money:
                            number_of_bouquets += 1
                else:
                    for c in range(0, int(money/flowers[0])+1, 2):
                        if (a*flowers[2] + b*flowers[1] + c*flowers[0]) > money:
                            break
                        if (a+b+c) > 0 and (a*flowers[2]+b*flowers[1]+c*flowers[0]) <= money:
                            number_of_bouquets += 1

    return number_of_bouquets

print "125 - %s" % bouquets(1,1,1,10)
print "79 - %s" % bouquets(1,2,1,10)
print "79 - %s" % bouquets(2,1,1,10)
print "0 - %s" % bouquets(3,4,5,2)
print "1 - %s" % bouquets(3,4,5,3)
print "3 - %s" % bouquets(3,4,5,5)
print "8 - %s" % bouquets(15.5,4.1,5.99,21.75)
print "51 - %s" % bouquets(21.25,13.6,10.5,100)
print "3462847 - %s" % bouquets(10,199,99,20000)
print "4666877 - %s" % bouquets(22,44,150,20000)


