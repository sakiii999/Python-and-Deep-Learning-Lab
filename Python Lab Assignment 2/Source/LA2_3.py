#Class Person is defined as class 1
class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
#Class student inherits class person by using OOPS concepts
class Student(Person):
    StudentCount = 0
    def __init__(self,name,email,student_id):
        Person.__init__(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        Person.display(self)
        print("Student Id: ",self.student_id)
#Class library inherits class person by using OOPS concepts
class Librarian(Person):
    StudentCount = 0
    def __init__(self,name,email,employee_id):
        super().__init__(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Details:")
        Person.display(self)
        print("Employee Id: ",self.employee_id)
#Class book has display function and __init__ has taken arguments
class Book():
    def __init__(self, bname, author, book_id):
        self.book_name = bname
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Details")
        print("BookName: ", self.book_name)
        print("Author: ", self.author)
        print("BookID: ", self.book_id)
#Class BookCheckout inherits Student and Books class by using multiple inheritance concept
class BookCheckout(Student,Book):
    def __init__(self, name, email, student_id, bname, author, book_id):
        Student.__init__(self,name,email,student_id)
        Book.__init__(self, bname, author, book_id)
    def display(self):
        print("Book details: ")
        Student.display(self)
        Book.display(self)
samplelist= []
#All details are appended in a single list and called
samplelist.append(Student('Saketh', 'sakethgaruda@gmail.com', 1234))
samplelist.append(Student('Pujita', 'pm47c@mail,umkc.edu', 5678))
samplelist.append(Librarian('Veda', 'bvbhaskar92@gmail.com', 1357))
samplelist.append(Librarian('Sudheesha', 'sudheesha@gmail.com', 9987))
samplelist.append(Book('Environmental Science', 'Pujita Mullapudi', 1937492))
samplelist.append(Book('Brain Eating', 'Veda', 938493))
samplelist.append(BookCheckout('Atlas', 'Aditya', 8328, 'History', 'Sarat', 34422))
for obj, a in enumerate(samplelist):
    a.display()
    print("\n")
    if obj == len(samplelist)-1:
        a.displayCount()