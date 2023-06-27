# Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.

soA = float(input('Nhap so thap phan a: '))
soB = int(input('Muon lam tron den chu so thu may: '))

print(f"So a: {soA} sau khi lam tron {soB} chu so thap phan la: {round(soA,soB)}")
