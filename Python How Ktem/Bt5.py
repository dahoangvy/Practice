# Nhập số từ bàn phím
decimal = (input("Nhập số ở hệ thập phân: "))

# Chuyển đổi số từ hệ thập phân sang hệ bát phân

try:
    decimal=int(decimal)
    octal = oct(decimal)
    # Hiển thị số ở hệ bát phân
    print("Số ở hệ bát phân:", octal)
except:
    print('So khong hop le! ')

