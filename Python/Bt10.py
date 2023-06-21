# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại}
# Và xuất ra file output theo mẫu sau: “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”.

nhapTen = input("Nhap vao ten: ")
nhapTuoi = input('Nhap vao tuoi hien tai: ')

print(f'Vao 20 nam nua, tuoi cua {nhapTen} se la {int(nhapTuoi) + 20}')