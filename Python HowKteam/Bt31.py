# Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu (Phần 2).
# Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.

try:
    
    nhapN = int(input("Nhap n: "))
    if nhapN <1 or nhapN >9:
        print("Phai nhap so trong pham vi tu 1 den 9")
    else:
        for hang in range(nhapN):
            for cot in range(nhapN - hang, 0, -1):
                print(cot, end=" ")
            print()
except:
    print("Dau vao khong hop le")