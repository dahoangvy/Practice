# Viết chương trình hiển thị ra màn hình các số chia hết cho 5 (không quá 10 số) trong khoảng a, b.
# Với a, b là hai số nguyên nhập từ bàn phím (a <= b).

try:
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))

    if a > b:
        print('a phai be hon hoac bang b')
    else:
        list = []
        for num in range(a, b+1):
            if num % 5 == 0:

                list.append(num)
                if len(list) <10:
                    thongBao = 'Da in het cac so chia het cho 5'
                else:
                    thongBao = 'Da qua 10 so roi!'
                    break
            else:
                thongBao = "Khong co so nao chia het cho 5"
    list = map(str, list)
    print(' '.join(list))
    print(thongBao)
except:
    print('Dinh dang dau vao khong hop le!')