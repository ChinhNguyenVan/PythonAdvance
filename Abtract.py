# 1, Abtract class là gì?
# Abstract class là một class mà bên trong nó chứa một hoặc nhiều phương thức trừu tượng. Phương thức trừu tượng ở đây
# là một phương thức mà chúng ta chỉ được phép khai báo nó và không được phép viết code thực thi nó. Khi một class được
# khai báo ở dạng abstract thì nó sẽ không thể nào khởi tạo được, mà chỉ có thể khởi tạo được thông qua các class con
# của nó. Một class kế thừa lại abstract class thì phải khai báo lại toàn bộ các phương thức trừu tượng bên trong
# abstract class mà nó kế thừa.

# 2, Khai báo abstract class trong Python.
# Để có thể khai báo được một abstract class trong Python, thì class này bắt buộc phải được kế thừa từ một
# ABC(Abstract Base Classes) của Python

# Và để gọi được class này trong chương trình thì bạn phải import nó. Cú pháp import như sau:
# from abc import ABC
# Cú pháp khai báo abstract class:


# class ClassName(ABC):


#     # code
# Trong đó: ClassName là tên của abstract class mà bạn muốn khai báo.

# VD: Mình sẽ khai báo một lớp trừu tượng person.

from abc import ABC, abstractmethod


class PersonAbstact(ABC):
    name = None
    age = 0

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)


# Vì abstract class là một class, nên các bạn có thể hoàn toàn khai báo thuộc tính và phương thức như một class
# bình thường.

# 3, Khai báo phương thức abstract trong Python.
# Để có thể khai báo một abstract method - phương thức trừu tượng  trong Python thì chúng ta cần phải import thêm
# module abstractmethod ở trong package abc.

# Và một phương thức trừu tượng thì bắt buộc phải được khai báo ở trong lớp trừu tượng.

# Cú pháp:
class ClassName(ABC):
    # khai bao phuong thuc truu tuong
    @abstractmethod
    def methodName(self):
        pass

# Trong đó:
# @abstractmethod là bắt buộc, đây là cú pháp khai báo cho Python biết phía dưới là phương thức trừu tượng.
# methodName là tên của phương thức trừu tượng.


class Person1Abstact(ABC):
    name = None
    age = 0

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    @abstractmethod
    def getFull(self):
        pass
