# Viết chương trình nhập vào từ bàn phím tên và chiều cao (cm) của hai bạn. Hiển thị ra màn hình thông báo bạn nào cao hơn.
# Có xử lý ngoại lệ

tenBan1 = input("Nhap vao ten cua ban thu nhat: ")
caoBan1 = input('Nhap vao chieu cao(cm) cua ban thu nhat: ')

tenBan2 = input("Nhap vao ten cua ban thu hai: ")
caoBan2 = input('Nhap vao chieu cao(cm) cua ban thu hai: ')

try:
    caoBan1 = int(caoBan1)
    caoBan2 = int(caoBan2)
    if caoBan1 > caoBan2:
        print(f'{tenBan1} cao hon {tenBan2}')
    elif caoBan1 < caoBan2:
        print(f'{tenBan1} thap hon {tenBan2}')
    else:
        print(f'{tenBan1} và {tenBan2} cao bang nhau')
except:
    print('Nhap vao khong hop le')
