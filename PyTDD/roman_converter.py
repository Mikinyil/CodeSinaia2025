def roman_converter(num):
    if isinstance(num, int):
        if num == 0:
            return None
        else:
            n = []
            while num >= 1000:
                num = num - 1000
                n.append("M")
            while num >= 500:
                num = num - 500
                n.append("D")
            while num >= 400:
                num = num - 400
                n.append("CD")
            while num >= 100:
                num = num - 100
                n.append("C")
            while num >= 50:
                num = num - 50
                n.append("L")
            while num >= 40:
                num = num - 40
                n.append("XL")
            while num >= 10:
                num = num - 10
                n.append("X")
            while num >= 5:
                num = num - 5
                n.append("V")
            while num >= 4:
                num = num - 4
                n.append("IV")
            while num >= 1:
                num = num - 1
                n.append("I")
            result = "".join(n)
            return(result)