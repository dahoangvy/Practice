# Viết chương trình nhập vào ba số a, b, c. 
# Nếu a, b, c là ba cạnh của một tam giác thì kiểm tra và hiển thị ra màn hình loại của tam giác.

nhapCanh = input('Nhap vao 3 so a, b, c: ').split()

try:
    nhapCanh = map(float, nhapCanh)
    a, b, c = nhapCanh
    loai = None
    if(a+b > c and a+c > b  and b+c> a):
        if (a*a == b*b + c*c or b*b == a*a + c*c or (c*c == a*a + b*b)):
            loai = 'vuong'
        elif (a == b and a == c):
            loai = 'deu'
        elif (a == b or a == c or b == c):
            loai ='can'
        elif (a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b):
            loai = 'tu'
        else:
            loai = 'nhon'

        print(f'{a}, {b}, {c} la 3 canh cua 1 tam giac {loai}')
    else:
        print(f'{a}, {b}, {c} khong phai la ba canh cua mot tam giac')
except:
    print('Nhap vao khong hop le')