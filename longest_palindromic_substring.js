//Đề bài: Tìm ra chuỗi đối 

// bài này dùng cách kiểm tra cả 2 đầu của string

var longestPalindrome = function(s) {
	let newString = ''

	for (let i = 0; i < s.length; i++) {
		for (var j = s.length - 1 ; j >= 0; j--) {
			if (s[i] == s[j]) {
				if (i != j) {
					newString = s.substring(i,j+1)
					return newString
				}
			}
		}
	}
};

longestPalindrome('cbbd')