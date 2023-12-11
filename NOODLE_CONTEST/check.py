import os

def get_file_size(file_path):
    # Kiểm tra xem file có tồn tại không
    if os.path.exists(file_path):
        # Lấy dung lượng của file
        file_size = os.path.getsize(file_path)
        return file_size
    else:
        return None

if __name__ == "__main__":
    file_path = "NOODLE_CONTEST\BAI01.py"
    file_size = get_file_size(file_path)

    if file_size is not None:
        print(f"Dung lượng của file {file_path} là {file_size} bytes.")
    else:
        print(f"File {file_path} không tồn tại.")
