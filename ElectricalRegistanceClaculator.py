def serices():
    n = int(input("number of registor: "))
    t_registance=0
    for i in range(n):
        r = int(input(f"{i+1}th registor's registance: "))
        t_registance+=r
    print(f"total registance is {t_registance}")

def perallel():
    n = int(input("number of registor: "))
    t_registance=0
    for i in range(n):
        r = int(input(f"{i+1}th registor's registance: "))
        t_registance+=1/r
    total=1/t_registance
    print(f"total registance is {total}")

def serices_perallel():
    pass


def main():
    chose = int(input('''1.serices
2.perallel
3.series-perallel 
'''))
    match chose:
        case 1:
           serices()
        case 2:
            perallel()   
        case 3:
            serices_perallel()
        case _ :
            print("input valid number")

main()
    