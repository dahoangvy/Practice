# Cho vào 1 chuỗi s chứa các ký tự '(', ')', '{', '}', '[' and ']'
# Xách định chuỗi s có hợp lệ hay không?
# Chuỗi hợp lệ là chuỗi: 
# - Dấu ngoặc mở phải được đóng bằng dấu ngoặc cùng loại.
# - Dấu ngoặc mở phải được đóng theo đúng thứ tự
# - Mỗi dấu ngoặc đóng có một dấu ngoặc mở tương ứng cùng loại.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

def isValid(s):
    
    # Tạo 1 ngăn xếp để lưu dấu ngoặc mở
    nganXep = []
    
    # Tạo 1 dict để định nghĩa từng cặp dấu ngoặc
    capDauNgoac = {')': '(',
                   '}': '{',
                   ']': '['}
    
    for char in s:
        if char in capDauNgoac.values():
            nganXep.append(char)
        elif char in capDauNgoac.keys():
            if nganXep == [] or capDauNgoac[char] != nganXep.pop():
                return False
        else:
             return False
    
    return nganXep == []