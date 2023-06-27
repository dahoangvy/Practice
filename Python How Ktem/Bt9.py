# Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
# Tính tổng của dãy số và hiển thị ra màn hình (Có xử lý ngoại lệ đầu vào).

dayA = input('Nhap vao dãy số nguyên A: ')
listA = dayA.split(" ")

try:
    daySoA = map(int, listA)
    Tong = sum(daySoA)
    print(f'Tong cua day so vua nhap la: {Tong}')
except:
    print('Day so nhap vao khong hop le')