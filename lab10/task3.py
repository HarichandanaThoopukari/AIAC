class Employee:
    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    def increase_salary(self, percent: float) -> None:
        if percent < 0:
            raise ValueError("Percent increase must be non-negative.")
        self.__salary += self.__salary * percent / 100

    def __str__(self) -> str:
        return f"Employee: {self.__name}, Salary: {self.__salary:.2f}"

    def print_details(self) -> None:
        print(self)

# Example usage:
if __name__ == "__main__":
    emp = Employee("John Doe", 50000)
    emp.print_details()