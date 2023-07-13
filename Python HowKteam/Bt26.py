# Viết chương trình nhập vào bàn phím hai số nguyên a và b (a <= b). 
# Tính và hiển thị ra màn hình tổng các số trong khoảng a đến b. Yêu cầu sử dụng vòng lặp for.

try:
    a = int(input('Nhap vao so nguyen a: '))
    b = int(input('Nhap vao so nguyen b: '))
    if a >= b:
        thongBao = 'So thu nhat lon hon so thu hai!'
    else:
        listSoNguyenab = list(range(a,b+1))
        tong = 0
        for num in listSoNguyenab:
            tong = tong + num
            thongBao = tong
except:
    thongBao = 'Dau vao khong hop le'
print(thongBao)
