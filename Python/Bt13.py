# Viết chương trình nhập vào từ file input một câu chào hỏi làm quen với độ dài bất kỳ, mỗi từ nằm trên một dòng.
# Xuất ra file output câu chào hỏi vừa nhận được trên 1 dòng duy nhất, các từ cách nhau 1 khoảng trắng.
# Có xử lý ngoại lệ

try:
    with open('Bt13.inp', 'r') as fileIn:
    # Sử dụng phương thức read() để đọc toàn bộ file được input từ câu lệnh open ở trên
        listCau = fileIn.read()
        # Sử dụng phương thức splitlines() để tách chuỗi thành 1 list dựa trên ký tự kết thúc dòng.
        newList = listCau.splitlines()

        # Từ list mới tạo được ở trên, tiến hành join, sau đó tiếp tục split chuỗi mới để xóa ký tự trắng trong list
        chuoiMoi = ' '.join(newList)
        chuoiMoii = chuoiMoi.split()

        # Join kết quả lại thành câu trên 1 dòng
        final = ' '.join(chuoiMoii)
        print(final)

    with open('Bt13.oup', 'w') as fileOut:
        fileOut.write(final)
except:
    with open('Bt13.oup', 'w') as fileOut:
        fileOut.write('Nhap vao khong hop le')