class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.first_name}"

    def is_adult(self):
        return self.age >= 20

    def __str__(self):
        return f"{self.full_name()} ({self.age}歳)"
