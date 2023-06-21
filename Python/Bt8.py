# Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
# Tính tổng của dãy số và hiển thị ra màn hình.

daySo = input('Nhap dãy so nguyen: ')

# Phan tach string từ input tren thanh 1 list(danh sách) với hàm split()
listSoNguyen = daySo.split(' ')

# Từ dãy trên sử dụng hàm map() để duyệt qua từng phần tử trong list listSoNguyen và áp dụng phương thức ép kiểu sang int
soNguyen = map(int,listSoNguyen)

# Tính tổng bằng phương thức sum
tongDaySo = sum(soNguyen)

print(tongDaySo)


# Có thể làm theo cách khác 
daySo = input('Nhap dãy so nguyen: ')
Tong = 0
for num in daySo.split(' '):
    Tong = Tong + int(num)

print(f'Tổng của dãy số là: {Tong}')