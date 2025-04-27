class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours = None, rest_days = None, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours = None, rest_days = None, email = None):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name = None, hours = None, rest_days = None, email = None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        if self.hours is None:
            raise ValueError("Не удалось определить отработанные часы: нет входных данных")
        return self.hours * self.__class__.hourly_payment