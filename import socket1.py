import socket
import pandas as pd
import io

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    data = client_socket.recv(4096).decode()
    data_io = io.StringIO(data)
    df = pd.read_csv(data_io)

    print("Data received from server.")
    
    # Analysis and visualization
    mean_price = df['price'].mean()
    print(f"Mean price of products: {mean_price}")

    # Example visualization (this would be more detailed in practice)
    import matplotlib.pyplot as plt
    
    df.plot(x='name', y='price', kind='bar', title='Product Prices')
    plt.xlabel('Product')
    plt.ylabel('Price')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('product_prices.png')
    print("Plot saved as 'product_prices.png'.")

    client_socket.close()

if __name__ == '__main__':
    client_program()

