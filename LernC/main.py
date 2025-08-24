def cxc ():
    num1 = float(input (" กรอก ตัวเลขเเรกครับ : "))
    op = input ("ใส่เครื่องหมายครับ : ")
    num2 = float(input("ใส่ตัวเลขสองครับ : "))

    if op == "+" :
        print ("คำตอบคือ ", num1 + num2)

    elif op == "-":
        print("คำตอบคือ ", num1 -num2)

    elif op == "*":
        print ("คำตอบคือ ", num1 * num2)

    elif op == "/":
        print ("คำตอบคือ ", num1 / num2)

    else:
        print("what?")

cxc()