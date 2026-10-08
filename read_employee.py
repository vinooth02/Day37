def read_employee():

    with open("employees.txt", "r") as file:
        data = file.read()

    print(data)


read_employee()