# 1, Khai báo Class trong Python.
# Như các bạn đã được tìm hiểu thì một đối tượng có thể có một hoặc nhiều class và trong mỗi class thì lại chứa một
# hoặc nhiều các thuộc tính và các phương thức... Để khai báo một class trong Python thì mọi người sử dụng cú pháp sau:

# class className:
#    # code
# Trong đó, className là tên của class mà bạn muốn khai báo.

# VD:


# class Person:
#     # code

# 2, Khai báo thuộc tính trong Class.
# Như ở trên mình có nói thì một class có thể chứa một hoặc rất nhiều các thuộc tính bên trong. Thuộc tính trong class,
# cũng tương tự như biến ở trong lập trình hướng thủ tục. Để khai báo một thuộc tính trong class thì mọi người chỉ cần
# khai báo như khai báo một biến bình thường và lưu ý là nó phải nằm trong phạm vi của class.

# VD:


# class Person:
#     name = "Nguyễn Văn Chinh"
#     age = 21
#     male = True


# 3, Khai báo phương thức trong Class.
# Phương thức ở trong hướng đối tượng cũng tương tự như hàm ở trong lập trình hướng thủ tục và một class
# thì có thể không có hoặc có nhiều phương thức. Để khai báo một phương thức trong Python mọi người chỉ cần khai báo
# như khai báo một hàm bình thường, và lưu ý là phải khai báo trong phạm vi của class.

# VD:

class Person:
    # thuộc tính
    name = "Nguyễn Văn Chinh"
    age = 21
    male = True
    # phương thức

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setMale(self, male):
        self.male = male

    def getMale(self):
        return self.male


# 4, Khởi tạo class.
# Sau khi đã khai báo được class trong Python rồi, thì để khởi tạo nó mọi người sử dụng cú pháp sau:

# variableName = className()
# Trong đó:

# variableName là biến mà bạn muốn thể hiện lại đối tượng.
# className là class mà bạn muốn khởi tạo.
# VD: Mình sẽ khởi tạo class person ở trên.

# person = Person()
# Sau khi đã khởi tạo được class rồi thì biến được instane lại class đó sẽ có thể truy cập được các phần tử được cho phép trong class đó. Bằng cách sử dụng dấu . theo cú pháp sau:

#     # truy cap den thuoc tinh
# object.propertyName

# #truy cap den phuong thuc
# object.methodName()
# Trong đó:

# object là biến thể hiện lại object.
# propertyName là tên thuộc tính mà bạn muốn truy xuất.
# methodName là tên phương thức mà bạn muốn truy xuất.

# instance
person = Person()
# properties
print(person.name)
print(person.age)
print(person.male)
# methods
person.setName("Nguyễn Văn A")
print(person.getName())

person.setAge(21)
print(person.getAge())

person.setMale(True)
print(person.getMale())
