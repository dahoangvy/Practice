# Viết chương trình nhập vào ba số a, b, c. Hiển thị ra màn hình cho biết A, B, C có là ba cạnh của một tam giác hay không
# (Có xử lý ngoại lệ đầu vào).

try:
    nhapCanh = input('Nhap vao 3 canh cua tam giac cach nahu bang khoang trang: ').split()
    a,b,c = map(float, nhapCanh)

    if (a>0) and (b>0) and (c>0):
        if a+b>c and a+c>b and b+c>a:
            print(f'{a}, {b}, {c} la ba canh cua mot tam giac')
        else:
            print(f'{a}, {b}, {c} khong phai la ba canh cua mot tam giac')
    else:
        print('Cac canh cua tam giac phai lon hon 0!')
        
except:
    print('Dinh dang dau vao khong hop le!')
