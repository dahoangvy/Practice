# Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
# Tính tổng của dãy số và hiển thị ra màn hình (Có xử lý ngoại lệ đầu vào).

try:
    chuoiSo = input('Nhap vao day so: ')

    daySo = map(float, chuoiSo.split())
    print(sum(daySo))
except:
    print('Đầu vao không hợp lệ')