class Student:
    # [assignment] Skeleton class. Add your code here
    student = "Bob"

    def __init__(self):
        pass
        # self.name = "Bob"

    

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.tracks = tracks

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))

# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.set_score(20.90)
# Bob.get_score()
