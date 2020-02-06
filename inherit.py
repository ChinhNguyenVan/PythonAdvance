# Trong Python để khai báo một class kết thừa từ một hoặc nhiều class thì các bạn sử dụng cú pháp:


# class className(inherit1, inherit2, ...):

#     #code
# Trong đó: Cú pháp khai báo class thì mình đã giới thiệu với mọi người ở bài trước rồi.
# inherit1, inherit2, ... là tên của các class mà bạn muốn kế thừa.

class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def getName(self):
        print("Name: %s" % (self.name))

    def getAge(self):
        print("Age: %d" % (self.age))

    def getSex(self):
        print("Sex: %s" % (self.sex))


class Male(Person):
    sex = "Male"


male = Male("Nguyễn Văn Chinh", 21)
male.getName()
male.getAge()
male.getSex()

# 4, Ghi đè phương thức và thuộc tính.
# Trong trường hợp cả hai class cha và con tồn tại các thuộc tính và phương thức có cũng tên, thì trong Python
# sẽ nó sẽ ưu tiên thực thi và gọi các phương thức và thuộc tính khai báo trong class được khởi tạo.

# VD:


class Foo:
    name = 'Foo'

    def getName(self):
        print("Class: Foo")


class Bar(Foo):
    name = 'Bar'

    def getName(self):
        print("Class: Bar")


print(Foo().name)
Foo().getName()
print(Bar().name)
Bar().getName()

# Super()
# Trong trường hợp ở class con mà bạn muốn sử dụng đến các thành phần trong class cha thì bạn phải sử dụng hàm super theo cú pháp sau:

#     # Đối với thuộc tính.
# super().variableName
# # Đối với phương thức.
# super().methodName()


class Loo:
    name = 'Loo'

    def getName(self):
        print("Class: Loo")


class Lar(Loo):
    name = 'Lar'

    def getName(self):
        print("Atribute name = " + super().name)
        super().getName()


Lar().getName()

# 5, Đa kế thừa trong Python.
# Cũng giống như C++ thì Python cũng hỗ trợ chúng ta đa kế thừa.


class First:
    def getClass(self):
        print("Class Fist")


class Second(First):
    def getClass(self):
        super().getClass()
        print("Class Second")


class Third(Second):
    def getClass(self):
        super().getClass()


third = Third()
third.getClass()
