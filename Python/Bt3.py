# Viết chương trình hiển thị các từ theo yêu cầu ra màn hình: “Xin”, “chao!", “Toi", “ten", “la”, “{Tên của bạn}”. 
# Các từ cách nhau bởi “--” và {Tên của bạn} được nhập từ bàn phím.

ten = input("Nhap ten cua ban: ")

print("Xin", "chao!", "Toi", "ten", "la", ten, sep="--")

# Tham số sep dùng để xác định ký tự phân tách giữa các giá trị được in ra màn hình trong hàm print.
# Tham số này cho phép bạn tùy chỉnh cách các giá trị được phân tách khi in ra. Mặc định của sep là khoảng trắng: sep = " "