# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại}
# Và xuất ra file output theo mẫu sau: “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”.

# Sử dụng with trước open để không cần phải đóng file sau khi mở
with open('Bt10.inp', mode='r') as inp:
    ten = inp.readline().rstrip('\n')
    tuoi = int(inp.readline())

# Sử dụng mode "w" để viết lên file mới
with open('Bt10.out', mode ='w') as out:
    out.write(f'Vao 20 nam nua tuoi cua {ten} se la: {tuoi + 20}')