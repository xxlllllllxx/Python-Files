global_num = 100


def calculate():
    global global_num
    print(global_num)

    global_num = "MODIFIED"
    print(global_num)

calculate()
print(global_num)
