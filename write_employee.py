def write_employee():

    name = "Karan"
    salary = 40000
    department = "IT"

    with open("employees.txt", "w") as file:

        file.write("Name: " + name + "\n")
        file.write("Salary: " + str(salary) + "\n")
        file.write("Department: " + department)

    print("Employee information written successfully")


write_employee()