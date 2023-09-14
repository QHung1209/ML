
def is_lucky(n):
    # Chuyển số thành chuỗi để truy cập từng chữ số
    s = str(n)
    # Kiểm tra xem tất cả các chữ số có phải là 4 hoặc 7 không
    return all([x in ('4', '7') for x in s])


def is_almost_lucky(n):
    # Chuyển số thành chuỗi để truy cập từng chữ số
    s = str(n)
    # Đếm số lượng các chữ số may mắn (4 hoặc 7) trong số đó
    lucky_count = sum([2 for x in s if x in ('4', '7')])
    # Kiểm tra xem số lượng chữ số may mắn có là một số may mắn không
    return is_lucky(lucky_count)


# Nhập số nguyên dương n
n = int(input())

s = str(n)
# Đếm số lượng các chữ số may mắn (4 hoặc 7) trong số đó
lucky_count = sum([2 for x in s if x in ('4', '7')])
print(lucky_count)
