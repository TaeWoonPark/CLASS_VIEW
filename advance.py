class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 75:
            return 1500
        else:
            return 500

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# C-5 & C-6: entry_fee()
print(ken.entry_fee())       # → 1000
print(tom.entry_fee())       # → 1500
print(ieyasu.entry_fee())    # → 500
print(michelle.entry_fee())  # → 0

# C-7: タブ区切り
print(ken.info_tab())        # → Ken Tanaka\t15\t1000
print(tom.info_tab())        # → Tom Ford\t57\t1500
print(ieyasu.info_tab())     # → Ieyasu Tokugawa\t75\t500
print(michelle.info_tab())   # → Michelle Tanner\t3\t0

# C-8: パイプ区切り
print(ken.info_pipe())       # → Ken Tanaka|15|1000
print(tom.info_pipe())       # → Tom Ford|57|1500
print(ieyasu.info_pipe())    # → Ieyasu Tokugawa|75|500
print(michelle.info_pipe())  # → Michelle Tanner|3|0
