# 1, Phạm vi truy cập thuộc tính và phương thức.
# Như ở phần Học Python cơ bản mình cũng có giới thiệu với mọi người là biến trong lập trình Python thì có 2 loại là
# biến cục bộ và biến toàn cục đúng không ạ?

# Nhưng đó là với biến, ở đây trong lập trình hướng đối tượng nói chung và lập trình Python nói riêng thì các thành
# phần trong một đối tượng sẽ tồn tại ở 3 mức độ khác nhau là public, protected, private. 3 mức độ này cũng đại diện
# cho tính chất đóng gói của hướng đối tượng, còn đóng gói như nào thì hãy cùng tìm hiểu về các mức độ này...

# 2, Public
# -Public là trạng thái công khai nhất trong ba mức độ, khi một thành phần trong class được khai báo ở dạng public
# tức là chúng ta có thể sử dụng được thành phần đó từ bất kỳ đâu trong chương trình. Và để khai báo một thành phần
# trong class là public thì mọi người chỉ cần tuân thủ quy tắc sau:

#     Tên của thành phần không được bắt đầu bằng ký tự _ mà phải bắt đầu bằng chữ cái.

# VD: khai báo một thuộc tính và một phương thức ở dạng public và gọi nó ở các trường hợp khác nhau:


class Foo:
    # Khai báo thuộc tính ở dạng public
    name = "Foo"
    # Khai báo phương thức ở dạng public

    def getName(self):
        # gọi thành phần trong class
        print(self.name)


# gọi thành phần ngoài class
print(Foo().name)  # Foo
Foo().getName()  # Foo


class Bar(Foo):
    pass


# test
Bar().getName()  # Foo

# 2, Protected.
# Protected nằm ở mức độ thứ 2. Khi một thành phần trong class được khai báo là protected thì nó chỉ có phạm vi
# sử dụng ở trong class khởi tạo nó và class kế thừa từ class đó (class con)
# mà chúng ta sẽ không thể gọi được khi đứng từ bên ngoài class.
# Nhưng, bản chất trong Python không tồn tại loại phạm vi này, do đó chúng ta quy chuẩn nó về protected
# mà bản chất của nó vẫn là public.
# Để khai báo một thành phần là protected thì mọi người cần tuân theo quy tắc sau:

# Tên của thành phần phải được bắt đầu bằng 1 ký tự _.


class Boo:
    # Khai báo thuộc tính ở chuẩn protected
    _name = "Boo"
    # Khai báo phương thức ở chuẩn protected

    def _getName(self):
        # gọi thành phần trong class
        print(self._name)


# gọi thành phần ngoài class
print(Boo()._name)
Boo()._getName()


class Aar(Boo):
    pass


# test
Aar()._getName()

# 3, Private.
# Private là phạm vị hẹp nhất trong lập trình hướng đối tượng, khi một thành phần trong đối tượng được khai báo ở
# dạng private, thì nó chỉ có phạm vi hoạt động ở trong class khai báo nó mà thôi.

# Để khai báo một thành phần ở dạng private thì mọi người chỉ việc tuân thủ theo quy tắc sau:

# Tên cả thành phần phải được bắt đầu bằng 2 ký tự __.


class Aoo:
    # Khai báo thuộc tính ở chuẩn private
    __name = "Aoo"
    # Khai báo phương thức ở chuẩn private

    def __getName(self):
        # gọi thành phần trong class
        print(self.__name)
    # khai báo một phương thức ở dạng public để gọi thành phần private

    def get(self):
        self.__getName()


# gọi thành phần ngoài class
print(Aoo().__name)  # 'Aoo' object has no attribute '__name'
Aoo().__getName()
Aoo().get()


class Car(Aoo):
    def getNameinFoo(self):
        self.__getName()


# test
Car().getNameinFoo()
