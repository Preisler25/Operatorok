class Adatok:
    def __init__(self, list):
        self.num1 = int(list[0])
        self.op = list[1]
        self.num2 = int(list[2])

def ImportFromTXT(filename):
    temp = []
    f = open(filename, "r").read()
    lines = f.strip().split("\n")
    for i in lines:
        temp.append(Adatok(i.split(" "))) 
    return temp

def f3(list):
    temp = 0
    for i in list:
        if i.op == "mod":
            temp += 1
    return temp

def f4(list):
    for i in list:
        if i.num1%10 == 0 and i.num2%10 == 0:
            return f"Van"
    return f"Nincs"

def f5(list):
    opMap = dict()
    for i in list:
        if i.op not in opMap:
            opMap[i.op] = 0
        opMap[i.op] += 1
    return formatMap(opMap)

def formatMap(map):
    temp = ""
    for i in map:
        if i == "mod" or i == "div" or i == "/" or i == "-" or i == "+" or i == "*":
            temp += f"\n\t{i} --> {map[i]} db"
    return temp

def f6(obj):
    if obj.op == "mod":
        if obj.num2 == 0:
            return f"{obj.num1} {obj.op} {obj.num2} = Egyébb hiba"
        return f"{obj.num1} {obj.op} {obj.num2} = {obj.num1%obj.num2}"
    elif obj.op == "div":
        if obj.num2 == 0:
            return f"{obj.num1} {obj.op} {obj.num2} = Egyébb hiba"
        return f"{obj.num1} {obj.op} {obj.num2} = {obj.num1//obj.num2}"
    elif obj.op == "/":
        if obj.num2 == 0:
            return f"{obj.num1} {obj.op} {obj.num2} = Egyébb hiba!"
        return f"{obj.num1} {obj.op} {obj.num2} = {obj.num1/obj.num2}"
    elif obj.op == "-":
        return f"{obj.num1} {obj.op} {obj.num2} = {obj.num1-obj.num2}"
    elif obj.op == "+":
        return f"{obj.num1} {obj.op} {obj.num2} = {obj.num1+obj.num2}"
    elif obj.op == "*":
        return f"{obj.num1} {obj.op} {obj.num2} = {obj.num1*obj.num2}"
    else:
        return f"{obj.num1} {obj.op} {obj.num2} = Operátor hiba!"

def f7():
    while True:
        temp = input("7.feladat: Kérek egy kifejezést: ")
        if temp == "vége":
            break
        print(f6(Adatok(temp.split(" "))))

def f8(list, filename):
    f = open(filename, "w", encoding="utf-8")
    for i in list:
        f.write(f"{f6(i)}\n")

def main():
    main_list = ImportFromTXT("kifejezesek.txt")
    print(f"2. feladat: Kifejezések száma: {len(main_list)}")
    print(f"3. feladat: Kifejezések maradékos osztással: {f3(main_list)}")
    print(f"4. feladat: {f4(main_list)} ilyen kifejezés!")
    print(f"5. feladat: Statisztika: {f5(main_list)}")
    f7()
    f8(main_list, "eredmenyek.txt")
main()