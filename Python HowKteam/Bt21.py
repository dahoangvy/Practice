# Viết chương trình nhập vào hệ số a,b,c của phương trình bậc 2 và giải phương trình đó.
# Có xử lí ngoại lệ
import math

a,b,c = input('Nhap vao he so a, b, c: ').split()
x1 = 0
x2 = 0

try:
    a = float(a)
    b = float(b)
    c=float(c)
    if a == 0:
        if b==0:
            if c == 0:
                print("Phuong trinh vo so nghiem.")
            else:
                print('Phuong trinh vo nghiem')
        else:
            x1 = (-b)/(2*a)
            x2 = x1
            print(f'Phuong trinh co nghiem kep gia tri la: {x1}')
    else:
        delta = b**2 - (4*a*c)
        if delta > 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print(f'Phuong trinh co 2 nghiem la: x1 = {x1}, x2 = {x2}')
        elif delta == 0:
            x1 = -b/(2*a)
            print(f'Phuong trinh co nghiem kep x1 = x2 = {x1}')
        else:
            print('Phuong trinh vo nghiem')
except:
    print('Nhap vao khong hop le')