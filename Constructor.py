# 1, Phương thức khởi tạo - constructor.
# Phương thức khởi tạo là một phương thức đặc biệt ở trong class, phương thức này mặc định sẽ được gọi khi chúng
# ta khởi tạo class đó. Nó thường được dùng để khởi tạo các thuộc, xử lý phương thức hoặc là dùng để nhận các
# tham số truyền vào class khi khởi tạo.

# Để khai báo một phương thức khởi tạo trong class thì mọi người chỉ cần viết một hàm có tên là __init__ với
# cú pháp như sau:

# Cú pháp:


# class className:
#     def __init__(self, param1, param2, ...):

#         #
# Trong đó:

# className là tên của class.
# param1, param2, ... là các tham số chúng ta muốn nhận khi kèm khi khởi tạo class.

class Person:
    def __init__(self):
        print("Class person được khởi tạo!")


person = Person()

# ===========================================


class Person1:
    def __init__(self, name, age, male):
        print("Name: %s - Age: %d - Male: %d" % (name, age, male))


person1 = Person1('Nguyễn Văn Chinh', 21, True)


# 2, Phương thức hủy - deconstructor.
# Trái ngược với phương thức khởi tạo, thì phương thức hủy sẽ được gọi khi chúng ta hủy một class, hay nó cách khác
# nó luôn được thực thi cuối cùng khi chúng ta khởi tạo một class. Nó thường được dùng để giải phóng tài nguyên
# của class.

# Để khai báo một phương thức hủy trong class thì mọi người chỉ việc khai báo một phương thức có tên là __del__ với
# cú pháp sau:

# Cú pháp:


# def __del__(self):
#     # code
class Person2:
    def __init__(self, name, age, male):
        print("Class person được khởi tạo!")
        print("Name: %s - Age: %d - Male: %d" % (name, age, male))

    def __del__(self):
        print('Class Person được hủy')


person2 = Person2('Nguyễn Văn Chinh', 21, True)


class Person3:
    def __init__(self, name, age, male):
        print("Class person được khởi tạo!")
        self.name, self.age, self.male = name, age, male

    def getName(self):
        print("Name: %s" % (self.name))

    def getAge(self):
        print("Age: %d" % (self.age))

    def getMale(self):
        print("Male: %d" % (self.male))

    def __del__(self):
        print('Class Person được hủy')
        del self.name, self.age, self.male


person3 = Person3('Nguyễn Văn Chinh', 21, True)
person3.getName()
person3.getAge()
person3.getMale()
