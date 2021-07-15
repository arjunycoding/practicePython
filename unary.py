# Unairy Function
def unairy(lst):
    if isinstance(lst, list) == True:
        if lst == []:
            return True
        else:
            cLst = lst.copy()
            if lst[0].lower() == "m":
                cLst.pop(0)
                for i in cLst:
                    if cLst.pop().lower() == "o":
                        continue
                    else:
                        return False
                return True
            elif lst[0].lower() == "o":
                for i in cLst:
                    if cLst.pop().lower() == "o":
                        continue
                    else:
                        return False
                return True  
    else:
        return False


# Unairy Is Zero? Function
def uzero(lst):
    if isinstance(lst, list) == True:
        if lst == []:
            return True
        elif lst == ["m"] or lst == ["M"]:
            return True
        else:
            return False
    else:
        print("Not a list")
        return False

# Unairy Is Negitive? Function
def uisneg(lst):
    if isinstance(lst, list) == True:
        cLst = lst.copy()
        if lst == ["m"] or lst == ["M"]:
            return False
        elif lst == []:
            return False
        elif lst[0].lower() == "m":
            cLst.pop(0)
            for i in cLst:
                if cLst.pop().lower() == "o":
                    continue
                else:
                    return False
            return True
        else:
            return False
    else:
        print("Not a list")
        return False
# Unairy Is Positive? Function
def uispos(lst):
    if isinstance(lst, list) == True:
        cLst = lst.copy()
        if lst == ["m"] or lst == ["M"] or lst == []:
            return False
        elif lst[0].lower() == "o":
            for i in cLst:
                if cLst.pop().lower() == "o":
                    continue
                else:
                    return False
            return True
        else:
            return False
    else:
        print("Not a list")
        return False

# Unairy list to number
def u2n(lst):
    if isinstance(lst, list) == True:
        cLst = lst.copy()
        number = 0
        isNeg = False
        if uisneg(lst) == True:
            isNeg = True
            cLst.pop(0)
            for i in range(len(cLst)):
                if cLst.pop().lower() == "o":
                    number += 1
                else:
                    return "not a number"
        elif uispos(lst) == True:
            for i in range(len(cLst)):
                if cLst.pop(0).lower() == "o":
                    number += 1
                    print(isNeg, number)
        if isNeg == False:
            return number
        elif isNeg == True:
            return -number
    else:
        return "not a number"
def n2u(num):
    if isinstance(num, int) == True:
        unairyLst = []
        numStr = str(num)
        if numStr[0] == "-":
            unairyLst.append("m")
            for i in range(int(numStr[1])):
                unairyLst.append("o")
            return unairyLst
        elif numStr[0] == numStr:
            for i in range(int(numStr[0])):
                unairyLst.append("o")
            return unairyLst
    else:
        return "not a number"


lst = []
number = -2
unairyList = unairy(lst)
uzeroList = uzero(lst)
uisnegList = uisneg(lst)
uisposList = uispos(lst)
u2nList = u2n(lst)
n2uList = n2u(number)
print(f"Is {lst} a unairy number: {unairyList}")
print(f"Is {lst} a equal to zero: {uzeroList}")
print(f"Is {lst} a negitive number: {uisnegList}")
print(f"Is {lst} a positive number: {uisposList}")
print(f"{lst} in number: {u2nList}")
print(f"{number} in unairy: {n2uList}")