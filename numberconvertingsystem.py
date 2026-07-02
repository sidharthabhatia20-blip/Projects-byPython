#History
a = []
#decimal to other
def decimal_to_octal(c):
    if c == 0:
        a.append(f"decimal_to_octal: 0o0")
        return "0"
    b = ""
    while c != 0:
        d = c % 8
        b += str(d)
        c //= 8
    a.append(f"decimal_to_octal: 0o{b[::-1]}")
    return b[::-1]

def decimal_to_binary(c):
    if c == 0:
        a.append(f"decimal_to_binary: 0b0")
        return "0"
    b = ""
    while c != 0:
        d = c % 2
        b += str(d)
        c //= 2
    a.append(f"decimal_to_binary: 0b{b[::-1]}")
    return b[::-1]

def decimal_to_hexadecimal(c):
    if c == 0:
        a.append(f"decimal_to_octal: 0x0")
        return "0"
    b = ""
    while c != 0:
        d = c % 16
        if d >= 10:
            b += chr(d+55)
        else:
            b += str(d)
        c //= 16
    a.append(f"decimal_to_hexadecimal: 0x{b[::-1]}")
    return b[::-1]

#other to decimal
def octal_to_decimal(c):
    if c == 0:
        a.append(f"octal_to_decimal: 0")
        return "0"
    i = 0
    s = 0
    while c != 0:
        d = c % 10
        if d < 0 or d > 7:
            print("Error: Octal should be 0 to 7")
            return
        s += d*(8**i)
        c //= 10
        i += 1
    print(f"octal to decimal: {s}")
    a.append(f"octal_to_decimal: {str(s)}")
    return s

def binary_to_decimal(c):
    if c == 0:
        a.append(f"binary_to_decimal: 0")
        return "0"
    i = 0
    s = 0
    while c != 0:
        d = c % 10
        if d < 0 or d > 1:
            print("Error: binary should be 0 or 1")
            return
        s += d*(2**i)
        c //= 10
        i += 1
    print(f"binary to decimal: {s}")
    a.append(f"binary_to_decimal: {str(s)}")
    return s

def hexadecimal_to_decimal(c):
    if c == "0":
        a.append(f"hexadecimal_to_decimal: 0")
        return "0"
    s = 0
    j = 0
    for i in range(len(c)-1, -1, -1):
        if '0' <= c[i] <= '9':
            s += int(c[i])*(16**j)
        elif 'A' <= c[i].upper() <= 'F' :
            s += (ord(c[i].upper())-55)*(16**j)
        else:
            print("Error: Hexadecimal should be 0 to 9 or A to F")
            return
        j += 1
    
    print("hexadecimal to decimal:",s)
    a.append(f"hexadecimal_to_decimal: {s}")
    return s

# Other base to other base
def octal_to_binary(c):
    binary = decimal_to_binary(octal_to_decimal(c))
    a.pop(-1)
    a.pop(-1)
    a.append(f"octal_to_binary: 0b{binary}")
    print(f"Octal to binary: 0b{binary}")

def octal_to_hexadecimal(c):
    hexadecimal = decimal_to_hexadecimal(octal_to_decimal(c))
    a.pop(-1)
    a.pop(-1)
    a.append(f"octal_to_hexadecimal: 0x{hexadecimal}")
    print(f"Octal to hexadecimal: 0x{hexadecimal}")

def binary_to_octal(c):
    octal = decimal_to_octal(binary_to_decimal(c))
    a.pop(-1)
    a.pop(-1)
    a.append(f"binary_to_octal: 0o{octal}")
    print(f"binary to octal: 0o{octal}")

def binary_to_hexadecimal(c):
    hexadecimal = decimal_to_hexadecimal(binary_to_decimal(c))
    a.pop(-1)
    a.pop(-1)
    a.append(f"binary_to_hexadecimal: 0x{hexadecimal}")
    print(f"binary to hexadecimal: 0x{hexadecimal}")

def hexadecimal_to_binary(c):
    binary = decimal_to_binary(hexadecimal_to_decimal(c))
    a.pop(-1)
    a.pop(-1)
    a.append(f"hexadecimal_to_binary: 0b{binary}")
    print(f"hexadecimal to binary: 0b{binary}")

def hexadecimal_to_octal(c):
    octal = decimal_to_octal(hexadecimal_to_decimal(c))
    a.pop(-1)
    a.pop(-1)
    a.append(f"hexadecimal_to_octal: 0o{octal}")
    print(f"hexadecimal to octal: 0o{octal}")

print("1) Decimal to octal")
print("2) Decimal to binary")
print("3) Decimal to hexadecimal")
print("4) octal to Decimal")
print("5) Binary to Decimal")
print("6) Hexadecimal to Decimal")
print("7) Octal to binary")
print("8) Octal to hexadecimal")
print("9) Binary to octal")
print("10) Binary to hexadecimal")
print("11) Hexadecimal to Binary")
print("12 Hexadecimal to octal")
print("13) Exit")

while True:
    ch = int(input("Enter choice: "))
    if ch == 1:
        c = int(input("Enter number: "))
        print(decimal_to_octal(c))
    elif ch == 2:
        c = int(input("Enter number: "))
        print(f"0b{decimal_to_binary(c)}")
    elif ch == 3:
        c = int(input("Enter number: "))
        print(f"0x{decimal_to_hexadecimal(c)}")
    elif ch == 4:
        c = int(input("Enter number: "))
        octal_to_decimal(c)
    elif ch == 5:
        c = int(input("Enter number: "))
        binary_to_decimal(c)
    elif ch == 6:
        c = input("Enter number/alphabet: ")
        hexadecimal_to_decimal(c)
    elif ch == 7:
        c = int(input("Enter number: "))
        octal_to_binary(c)
    elif ch == 8:
        c = int(input("Enter number: "))
        octal_to_hexadecimal(c)
    elif ch == 9:
        c = int(input("Enter number: "))
        binary_to_octal(c)
    elif ch == 10:
        c = int(input("Enter number: "))
        binary_to_hexadecimal(c)
    elif ch == 11:
        c = input("Enter number/Alphabet: ")
        hexadecimal_to_binary(c)
    elif ch == 12:
        c = input("Enter number/Alphabet: ")
        hexadecimal_to_octal(c)
    elif ch == 13:
        break
    print("\nHistory:\n")
    for i in range(len(a)):
        print(a[i])