# Viết chương trình tính tổng 2 số nguyên nhập vào từ bàn phím có xử lý trường hợp ngoại lệ

a = (input("Nhap sô nguyen a: "))
b = (input("Nhap sô nguyen b: "))
try:
    a = int(a)
    b = int(b)
    c = a+b
    print(f"Tong cua 2 so là {c}")
except:
    print("Nhap sai so")

# hàm try except dùng để xử lý các ngoại lệ
# Mã bên trong khối try được thực thi.
# Nếu không có ngoại lệ xảy ra, các câu lệnh trong khối try sẽ được thực thi hết và khối except sẽ được bỏ qua.
# Nếu một ngoại lệ xảy ra trong khối try, luồng điều khiển sẽ được chuyển đến khối except phù hợp với kiểu ngoại lệ tương ứng.
# Mã bên trong khối except sẽ được thực thi để xử lý ngoại lệ.