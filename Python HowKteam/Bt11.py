# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại}
# Và xuất ra file output theo mẫu sau: “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. Có xử lý ngoại lệ

# Cung tương tự sử dụng witn + open để mở file Bt11.inp, khi dùng with chương trình sẽ tự động đóng file được mở.
with open('Bt11.inp', 'r') as inp:
    ten = inp.readline().rstrip('\n')
    tuoi = inp.readline()

try:
    tuoi = int(tuoi)
    with open('Bt11.out', 'w') as out:
        out.write(f'Vao 20 nam nua tuoi cua {ten} se la: {tuoi + 20}')
except:
    with open('Bt11.out', 'w') as out:
        out.write('Nhap vao khong hop le')