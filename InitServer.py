
# 1, Tạo một con server đơn giản.
# Đầu tiên để có thể khởi tạo được một con server thì bạn cần import module htttp.server của Python vào trong
# chương trình:
# from http.server import BaseHTTPRequestHandler, HTTPServer
# Và ở đây chúng ta cần sử dụng đến 2 object BaseHTTPRequestHandler, HTTPServer trong module http.server.

# Tiếp đó chúng ta sẽ khai báo một class kế thừa từ class BaseHTTPRequestHandler của Python.
# Và khai báo thêm một phương thức do_GET() để xử lý khi có get Request gửi lên.


from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class


class SimpleHTTP(BaseHTTPRequestHandler):

    # Nhận GET request gửi lên.
    def do_GET(self):
        # SET http status trả về
        self.send_response(200)

        # Thiết lập header trả về
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Data
        message = "Hoc Lap Trinh Tai Toidicode.com"
        # Write data dưới dạng utf8
        self.wfile.write(bytes(message, "utf8"))
        return


# cấu hình host và cổng port cho server
server_address = ('127.0.0.1', 8000)

# Khởi tạo server với thông số cấu hình ở trên.
httpd = HTTPServer(server_address, SimpleHTTP)

# Tiến hành chạy server
httpd.serve_forever()
