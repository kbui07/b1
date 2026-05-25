# a. Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
# Vì chuỗi trong python là bất biến
# b. Vì sao student_name.title() không tạo ra "Nguyen Van A"?
# Vì title chỉ trả về chuỗi mới
# c. Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
# Vì upper kh trực tiếp sửa chuỗi
# d. Vì sao email.lower() không làm email chuyển thành chữ thường?
# Vì trả về chuỗi mới kh lưu
# e. Muốn các phương thức xử lý chuỗi có hiệu lực cần làm gì?
# Gán các kết quả lại vào biến

student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)