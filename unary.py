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
        print("not a list")
        return False
# Check If Both The Unairy List Are A unariy List Function
def bothunary(lst1, lst2):
    unairy1 = unairy(lst1)
    unairy2 = unairy(lst2)
    if unairy1 == True and unairy2 == True:
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
        if isNeg == False:
            return number
        elif isNeg == True:
            return -number
    else:
        return "not a list"
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
            for i in range(int(numStr)):
                unairyLst.append("o")
            return unairyLst
    else:
        return "not a number"

def uneg(lst):
    if unairy(lst) == True:
        cLst = lst.copy()
        if uisneg(lst) == True:
            cLst.pop(0)
            return cLst
        elif uispos(lst) == True:
            cLst[0:0] = ["m"]
            return cLst
    else:
        return "not a unary list"

def uabs(lst):
    if unairy(lst) == True:
        cLst = lst.copy()
        if uisneg(lst) == True:
            cLst.pop(0)
            return cLst
        elif uispos(lst) == True:
            return cLst
    else:
        return "not a unary list"
def uequal(lst1, lst2):
    if bothunary(lst1, lst2) == True:
        if uispos(lst1) and uisneg(lst2) or uisneg(lst1) and uispos(lst2):
            return False
        elif uispos(lst1) and uispos(lst2):
            lenOfLst1 = len(lst1)
            lenOfLst2 = len(lst2)
            if lenOfLst1 == lenOfLst2:
                return True
            else:
                return False
        elif uisneg(lst1) and uisneg(lst2):
            lenOfLst1 = len(lst1)
            lenOfLst2 = len(lst2)
            if lenOfLst1 == lenOfLst2:
                return True
            else:
                return False
        elif uzero(lst1) and uzero(lst2) == True:
            return True
        else:
            return False
    else:
        return "not a unairy list"
def une(lst1, lst2):
    if uequal(lst1, lst2) == True:
        return False
    elif uequal(lst1, lst2) == False:
        return True

def ugt(lst1, lst2):
    if bothunary(lst1, lst2) == True:
        isGreater = len(lst1) > len(lst2)
        if uispos(lst1) and uispos(lst2) == True:
            return len(lst1) > len(lst2)
        elif uisneg(lst1) and uisneg(lst2) == True:
            if isGreater == True:
                return False
            elif isGreater == False:
                return True
        elif uispos(lst1) and uisneg(lst2) == True:
            return True
        elif uisneg(lst1) and uispos(lst2) == True:
            return False
        elif uzero(lst1) and uzero(lst2) == True:
            return False
        elif uzero(lst1) and uispos(lst2) == True:
            return False
        elif uzero(lst1) and uisneg(lst2) == True:
            return True
        elif uzero(lst2) and uispos(lst1) == True:
            return True
        elif uzero(lst2) and uisneg(lst1) == True:
            return False 
    else:
        return "not a unary list" 

def ugte(lst1, lst2):
    if bothunary(lst1, lst2) == True:
        if ugt(lst1, lst2) == True or uequal(lst1, lst2) == True:
            return True
        else:
            return False
    else:
        return "not a unairy list"
def uls(lst1, lst2):
    if bothunary(lst1, lst2) == True:
        if ugt(lst1, lst2) == True:
            return False
        else:
            return True
    else:
        return "not a unairy number"
def ulse(lst1, lst2):
    if bothunary(lst1, lst2) == True:
        if uls(lst1, lst2) == True or uequal(lst1, lst2) == True:
            return True
        else:
            return False
    else:
        return "not a unairy number"

def uinc(lst):
    if unairy(lst):
        cLst = lst.copy()
        if uispos(lst) == True:
            cLst.append("o")
            return cLst
        elif uisneg(lst) == True:
            cLst.pop(len(cLst) - 1)
            if uzero(cLst):
                cLst = []
            return cLst
        elif uzero(cLst):
            cLst = ["o"]
            return cLst
    else:
        return "not a unairy list"
def udec(lst):
    if unairy(lst):
        cLst = lst.copy()
        if uispos(lst) == True:
            cLst.pop()
            if uzero(cLst):
                cLst = []
                return cLst
            return cLst
        elif uisneg(lst) == True:
            cLst.append("o")
        elif uzero(cLst):
            cLst = ["m", "o"]
            return cLst
    else:
        return "not a unairy list"

lst1 = ["o", "o"] # -2
lst2 = [] # -3
print(udec(lst1))