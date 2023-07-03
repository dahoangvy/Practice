# Viết chương trình nhập vào từ file input ba số a, b, c. 
# Nếu a, b, c là ba cạnh của một tam giác thì kiểm tra và xuất ra file output thông báo loại của tam giác (Có xử lý ngoại lệ đầu vào).

with open('Python HowKteam\Bt23.inp', "r") as inPut:
    baCanh = inPut.readline().strip().split()
try:
    a,b,c = map(float, baCanh)
    loai = None
    if(a+b > c and a+c > b  and b+c> a):
        if (a*a == b*b + c*c or b*b == a*a + c*c or (c*c == a*a + b*b)):
            loai = 'vuong'
        elif (a == b and a == c):
            loai = 'deu'
        elif (a == b or a == c or b == c):
            loai ='can'
        elif (a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b):
            loai = 'tu'
        else:
            loai = 'nhon'
        with open('Python HowKteam\Bt23.oup', "w") as outPut:
            outPut.write(f'{a}, {b}, {c} la ba canh cua mot tam giac {loai}')
    else:
        with open('Python HowKteam\Bt23.oup', "w") as outPut:
            outPut.write(f'{a}, {b}, {c} không la ba canh cua mot tam giac')
except:
    with open('Python HowKteam\Bt23.oup', "w") as outPut:
            outPut.write('Nhap vao khong hop le')