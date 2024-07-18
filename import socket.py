import socket
import json

# تنظیمات سرور
HOST = '127.0.0.1' # آدرس IP سرور
PORT = 65432 # پورت سرور

# ایجاد سوکت
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is listening on", HOST, PORT)

while True:
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        if not data:
            break
        # کراول کردن داده‌ها (نمونه ساده)
        products_data = {
            'your_products': [
                {'name': 'Product1', 'initial_price': 100, 'selling_price': 120, 'profit': 20},
                {'name': 'Product2', 'initial_price': 200, 'selling_price': 250, 'profit': 50}
            ],
            'competitor_products': [
                {'name': 'Product1', 'price': 110},
                {'name': 'Product2', 'price': 240}
            ]
        }
        conn.sendall(json.dumps(products_data).encode('utf-8'))

