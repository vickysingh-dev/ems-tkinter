from database import fetch


class Employee:

    def __init__(self):
        pass

    # def __init__(self, first, last, designation, email, phone, doj, gender, salary) -> None:
    #     self.first = first
    #     self.last = last
    #     self.designation = designation
    #     self.email = email
    #     self.phone = phone
    #     self.doj = doj
    #     self.gender = gender
    #     self.salary = salary

    def fetch_data(self):
        fetch_string = 'SELECT * FROM employee;'
        result = fetch(fetch_string)
        print(result)


emp = Employee()
emp.fetch_data()
