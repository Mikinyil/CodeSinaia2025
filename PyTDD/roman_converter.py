def roman_converter(num):
    VALUES = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),   
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    # VALUES2 = [
    #     (1000, "thousand"),
    #     (100, "hundred"),
    #     (90, "ninety"),
    #     (80, "eighty"),
    #     (70, "seventy"),
    #     (60, "sixty"),
    #     (50, "fifty"),
    #     (40, "forty"),
    #     (30, "thirty"),
    #     (20, "twenty"),
    #     (19, "nineteen"),
    #     (18, "eighteen"),
    #     (17, "seventeen"),
    #     (16, "sixteen"),
    #     (15, "fifteen"),
    #     (14, "fourteen"),
    #     (13, "thirteen"),
    #     (12, "twelve"),
    #     (11, "eleven"),
    #     (10, "ten"),
    #     (9, "nine"),
    #     (8, "eight"),
    #     (7, "seven"),
    #     (6, "six"),
    #     (5, "five"),
    #     (4, "four"),
    #     (3, "three"),
    #     (2, "two"),
    #     (1, "one")
    # ]

    if isinstance(num, int):
        if num <= 0:
            return None
        else:
            # n = []
            # while num >= 1000:
            #     num = num - 1000
            #     n.append("M")
            # while num >= 900:
            #     num = num - 900
            #     n.append("CM")
            # while num >= 500:
            #     num = num - 500
            #     n.append("D")
            # while num >= 400:
            #     num = num - 400
            #     n.append("CD")
            # while num >= 100:
            #     num = num - 100
            #     n.append("C")
            # while num >= 90:
            #     num = num - 90
            #     n.append("XC")
            # while num >= 50:
            #     num = num - 50
            #     n.append("L")
            # while num >= 40:
            #     num = num - 40
            #     n.append("XL")
            # while num >= 10:
            #     num = num - 10
            #     n.append("X")
            # while num >= 9:
            #     num = num - 9
            #     n.append("IX")
            # while num >= 5:
            #     num = num - 5
            #     n.append("V")
            # while num >= 4:
            #     num = num - 4
            #     n.append("IV")
            # while num >= 1:
            #     num = num - 1
            #     n.append("I")
            # result = "".join(n)

            #===========================================

            result = ""
            for value, numeral in VALUES:
                while num >= value:
                    num -= value
                    result += numeral

            #===========================================
            # result = ""
            # for value, numeral in VALUES:
            #     n=0
            #     while num >= value:
            #         num -= value
            #         n+=1
            #     if n == 1:
            #         result += numeral
            #     elif n > 1:
            #         result += " " + n + " " + numeral
            #===========================================
            return(result)