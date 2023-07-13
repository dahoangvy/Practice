# Viết chương trình hiển thị ra màn hình bảng cửu chương n. Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím
try:
    nhapN = int(input('Nhap so nguyen n: '))
    if nhapN > 9 or nhapN < 1:
        print('Chi tinh duoc bang cuu chuong 1 den 9 thoi!')
    else:
        for i in range(1,11):
            print(f'{nhapN} x {i} = {nhapN*i}')
except:
    print('Dau vao khong hop le!')