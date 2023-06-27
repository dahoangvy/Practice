# Viết chương trình nhập vào ba số a, b, c. Hiển thị ra màn hình cho biết a, b, c có là ba cạnh của một tam giác hay không.

# Sử dụng phương thức split() để tách chuỗi nhập vào từ input thành 1 list
nhapCanh = input("Nhap 3 canh a, b, c: ").split()

# Sử dụng hàm map để ép kiểu cho toàn bộ cạnh của tam giác vừa nhập vào sang kiểu float
a, b, c = map(float, nhapCanh)

if (a + b > c) and (a + c > b) and (b+c >a):
    print(f'{a}, {b}, {c} la ba canh cua mot tam giac')
else:
    print(f'{a}, {b}, {c} khong la ba canh cua mot tam giac')