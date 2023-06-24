# Viết chương trình nhập vào từ file input một câu chào hỏi làm quen với độ dài bất kỳ, mỗi từ nằm trên một dòng.
# Xuất ra file output câu chào hỏi vừa nhận được trên 1 dòng duy nhất, các từ cách nhau 1 khoảng trắng.

with open('Bt12.inp', 'r') as fileIn:
    # Sử dụng hàm read() để đọc toàn bộ file được input từ câu lệnh open ở trên
    toanBoCau = fileIn.read()

    # Sử dụng phương thức splitlines() để tách chuỗi thành 1 list các dòng dựa trên ký tự kết thúc dòng
    listCau = toanBoCau.splitlines()

with open('Bt12.oup', 'w') as fileOut:
    # Sử dụng phương thức join để join list thành 1 chuỗi
    cauHoanChinh = (' ').join(listCau)
    fileOut.write(cauHoanChinh)