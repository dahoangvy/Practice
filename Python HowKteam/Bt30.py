# Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu. 
# Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.

try:
    
    nhapN = int(input("Nhap n: "))
    if nhapN <1 or nhapN >9:
        print("Phai nhap so trong pham vi tu 1 den 9")
    else:
        for hang in range(1, nhapN+1):
            for cot in range(1, hang+1):
                print(cot, end=" ")
            print()
except:
    print("Dau vao khong hop le")