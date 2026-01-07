from .student import Student

class StudentProxy(Student):
    class Meta:
        proxy = True
    def is_adult(self):
        return self.age >= 18
