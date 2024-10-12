# khi đưa vào chuỗi kí tự và số hàng bạn muốn

class Solution:
    def convert(self,s, numRows):

        # kiểm tra nếu chỉ có 1 dòng thì in ra luôn
        # "len(s) <= numRows": đoạn này không có cũng được
        # nhưng nên thêm vào để tối ưu hiệu 
        if numRows == 1 or len(s) <= numRows:
                return s

        # bao nhiêu dòng thì đồng với bấy nhiêu phần tử trong mảng
        rows = [''] * numRows

        # dòng hiện tại đang đứng
        cur_row = 0

        # đang xuống hoặc đi lên
        going_down = False

        for char in s:
                rows[cur_row] += char

                if cur_row == 0 or cur_row == numRows - 1:
                        going_down = not going_down
                cur_row += 1 if going_down else -1

        return ''.join(rows)






solution = Solution()
print(solution.convert("PAYPALISHIRING", 100))
