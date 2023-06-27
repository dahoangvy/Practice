# Viết chương trình nhập vào từ bàn phím lần lượt số thứ nhất, phép tính, số thứ 2 cách nhau bằng khoảng trắng để tính toán theo phép tính được nhập

nhapVao = (input('Nhập vào lần lượt số thứ 1, phép toán, số thứ 2, cách nhau bằng khoảng trắng: ').split())
try:
    soThu1 = float(nhapVao[0])
    soThu2 = float(nhapVao[2])
    phepTinh = nhapVao[1]
    ketQua = None
    
    if phepTinh == "+":
        ketQua = soThu1 + soThu2
    elif phepTinh == "-":
        ketQua = soThu1 - soThu2
    elif phepTinh =='*':
        ketQua = soThu1*soThu2
    elif phepTinh == '/':
        if soThu2 == 0:
            print('So bi chia phai khac 0')
        else:
            ketQua = soThu1/soThu2
    if ketQua != None:
        print(f'Ket qua cua phep tinh {soThu1} {phepTinh} {soThu2} la: {ketQua}')
except:
    print('Đầu vào không hợp lệ')