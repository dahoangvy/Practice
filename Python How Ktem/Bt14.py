# Viết chương trình nhập vào từ bàn phím tên và chiều cao (cm) của hai bạn. Hiển thị ra màn hình thông báo bạn nào cao hơn.

tenBan1 = input("Nhap vao ten cua ban thu nhat: ")
caoBan1 = input('Nhap vao chieu cao(cm) cua ban thu nhat: ')

tenBan2 = input("Nhap vao ten cua ban thu hai: ")
caoBan2 = input('Nhap vao chieu cao(cm) cua ban thu hai: ')

if int(caoBan1) > int(caoBan2):
    print(f'Ban {tenBan1} cao hon ban {tenBan2}')
else:
    print(f'Ban {tenBan2} cao hon ban {tenBan1}')