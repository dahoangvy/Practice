# Viết chương trình giải phương trình bậc nhất và phương trình bậc hai với các hệ số được nhập từ file input và kết quả được xuất ra file output (Có xử lý ngoại lệ đầu vào)
import math
try:
    with open('Bt24.inp', 'r') as fileIn:
        dong1 = int(fileIn.readline())
        dong2 = fileIn.readline().split()

        # Giai phuong trinh bac 1
        if dong1 == "1":
            a, b = map(float, dong2)
            if a != 0:
                if b != 0:
                    x = -b/a
                    thongBao = (f'Nghiem cua phuong trinh bac 1: ax + b = 0, voi a = {a}, va b = {b} la: {x}')
                else:
                    thongBao = ('Phuong trinh vo so nghiem')
            else:
                thongBao = (f'Phuong trinh vo nghiem voi a = 0')

        # Gia phuong trinh bac 2
        elif dong1 == "2":
            a, b, c = map(float, dong2)

            if a == 0:
                if b==0:
                    if c == 0:
                        thongBao = 'Phuong trinh vo so nghiem'
                    else:
                        thongBao = 'Phuong trinh vo nghiem'
                else:
                    x1 = (-b)/(2*a)
                    x2 = x1
                    thongBao = (f'Phuong trinh co nghiem kep gia tri la: {x1}')
            else:
                delta = b**2 - (4*a*c)
                if delta > 0:
                    x1 = (-b + math.sqrt(delta))/(2*a)
                    x2 = (-b - math.sqrt(delta))/(2*a)
                    thongBao = (f'Phuong trinh co 2 nghiem la: x1 = {x1}, x2 = {x2}')
                elif delta == 0:
                    x1 = -b/(2*a)
                    thongBao = (f'Phuong trinh co nghiem kep x1 = x2 = {x1}')
                else:
                    thongBao = ('Phuong trinh vo nghiem')
except FileNotFoundError:
    thongBao = 'Khong tim thay file nhap vao'

except: 
    thongBao = 'Nhap vao khong hop le'

with open('Bt24.oup', 'w') as fileOut:
    fileOut.write(thongBao)
                    