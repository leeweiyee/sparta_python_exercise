# Sparta University - Python Project
# As a user I want to create a trainee
# As a user I want to add a student to a batch
# As a user I want to list all modules
# As a user I want to list all students in a batch

class Batch():

    list_of_students = ['Weiyee', 'CJ', 'Gigi']

    def __init__(self):
        pass

    def list_all_students(self):
        print('List of student names:')
        for student in self.list_of_students:
            print(student)

    def add_student(self,name):
        self.list_of_students.append(name)
        print('Name successfully added.')
        print('Appended list of student names:')
        for student in self.list_of_students:
            print(student)

# As a user I want to list all students in a batch
student1 = Batch()
student1.list_all_students()

# As a user I want to add a student to a batch
student1.add_student('Isabella')


class Trainee():

    data_modules = ['Business week', 'SQL and Agile', 'Python development', 'Machine learning', 'Tableau']
    devops_modules = ['Business week', 'SQL', 'Web development', 'JavaScript', 'Linux', 'Virtual machines', 'Advanced patterns']

    def __init__(self,name,age,batch,stream):
        self.name = name
        self.age = age
        self.batch = batch
        self.stream = stream

    def create_trainee(self):
        print('A new trainee has been added.')
        return('{} is {} years old who is in the {} batch of the {} stream.'.format(self.name, self.age, self.batch, self.stream))

    def get_modules(self):
        if self.stream.lower() == "data":
            print('List of modules in Data stream:')
            for module in self.data_modules:
                print(module)

        elif self.stream.lower() == "devops":
            print('List of modules in DevOps stream:')
            for module in self.devops_modules:
                print(module)

        else:
            return('There is an error in the stream name.')

# As a user I want to create a trainee
trainee1 = Trainee('Weiyee', '20', 'Data 9', 'Data')
trainee1.create_trainee()

# As a user I want to list all modules
trainee1.get_modules()