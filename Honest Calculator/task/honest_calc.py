msg = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]
memory = 0
result = 0


def is_number(f):
    try:
        float(f)
        return True
    except ValueError:
        return False


def is_one_digit(v):
    v = str(v)
    if -10 < float(v) < 10:
        if "." in v:
            if int(v[v.find(".") + 1:]) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def check(v1, v2, v3):
    message = ""

    if is_one_digit(v1) and is_one_digit(v2):
        message += msg[6]
    if (float(v1) == 1 or float(v2) == 1) and v3 == "*":
        message += msg[7]
    if (float(v1) == 0 or float(v2) == 0) and v3 in "*+-":
        message += msg[8]
    if message != "":
        message = msg[9] + message
        print(message)


def save_result():
    if not is_one_digit(result):
        return True
    else:
        msg_index = 10
        while msg_index < 13:
            print(msg[msg_index])
            a = input()
            while a != "y" and a != "n":
                print(msg[msg_index])
                a = input()
            if a == "n":
                return False
            else:
                msg_index += 1
        return True


while True:
    while True:
        print(msg[0])
        calc = input()
        x, oper, y = calc.split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory

        if not is_number(x) or not is_number(y):
            print(msg[1])
            continue
        elif oper not in "+-*/":
            print(msg[2])
            continue

        check(x, y, oper)

        if oper == "+":
            result = float(x) + float(y)
            break
        elif oper == "-":
            result = float(x) - float(y)
            break
        elif oper == "*":
            result = float(x) * float(y)
            break
        else:
            try:
                result = float(x) / float(y)
                break
            except ZeroDivisionError:
                print(msg[3])
                continue

    print(result)

    print(msg[4])
    store_it = input()
    while store_it != "y" and store_it != "n":
        print(msg[4])
        store_it = input()
    if store_it == "y" and save_result():
        memory = result

    print(msg[5])
    continue_calcs = input()
    while continue_calcs != "y" and continue_calcs != "n":
        print(msg[5])
        continue_calcs = input()
    if continue_calcs == "n":
        break
