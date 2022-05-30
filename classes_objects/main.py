class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score): #
        self.name = str(name) 
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        print("The student's information is displayed below:")

    def change_name(self, new_name):
        self.name = new_name
        print('name is :', self.name)

    def change_age(self, new_age):
        self.age = new_age
        print(self.name,"'s age is :", self.age)

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(self.name,"'s new tracks : ", self.tracks)

    def get_score(self):
        print(self.name,"'s scores is :", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()