# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại}
# Và xuất ra file output theo mẫu sau: “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. Có xử lý ngoại lệ

nhapTen = input("Nhap vao ten: ")
nhapTuoi = input('Nhap vao tuoi hien tai: ')
try:
    tuoi = int(nhapTuoi)
    print(f'Vao 20 nam nua, tuoi cua {nhapTen} se la {(nhapTuoi) + 20}')
except:
    print('Nhap vao khong hop le!')