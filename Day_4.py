class Person(object):
    def __init__(self, initial_age):
        if initial_age < 0:
            print("This age for person is not valid, setting age to 0.")
        self.age = max(0, initial_age)

    def how_old_i_am(self):
        result = "You are {}."
        if self.age in range(0, 13):
            my_status = "young"
        elif self.age in range(13, 18):
            my_status = "teenager"
        else:
            my_status = "old"
        print(result.format(my_status))

    def year_passes(self):
        self.age += 1


for _ in range(int(input())):
    p = Person(int(input()))
    p.how_old_i_am()
    for j in range(0, 3):
        p.year_passes()
    p.how_old_i_am()
    print("")
