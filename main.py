class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    print("Information of the new student")

    def change_name(self,new_name):
        self.name = new_name
        print("Name:", self.name)

    def change_age(self,new_age):
        self.age = new_age
        print("Peter's age:", self.age)

    def add_track(self,new_tracks):
        self.track = new_tracks
        print("Peter's tracks:", self.track)
    
    def get_score(self, new_score):
        self.score = new_score
        print("Peter's score", self.score)
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(3.5)
