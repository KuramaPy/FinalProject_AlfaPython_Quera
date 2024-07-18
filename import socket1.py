import socket
import json

# تنظیمات کلاینت
HOST = '127.0.0.1' # آدرس IP سرور
PORT = 65432 # پورت سرور

# ایجاد سوکت
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# درخواست داده‌ها
client_socket.sendall(b'GET DATA')

data = client_socket.recv(1024)
client_socket.close()

# پردازش داده‌ها
products_data = json.loads(data.decode('utf-8'))
your_products = products_data['your_products']
competitor_products = products_data['competitor_products']

# نمایش داده‌ها
print("Your Products:", your_products)
print("Competitor Products:", competitor_products)


