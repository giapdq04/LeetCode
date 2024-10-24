
var longestCommonPrefix = function(strs) {

    // nếu như truyền vào 1 list 
    if (!strs.length) return "";

    // lấy chuỗi đầu tiên làm mốc
    // duyệt qua từng ký tự của chuỗi đầu trong mảng
    // và so sánh với các chuỗi còn 
    for (let i = 0; i < strs[0].length; i++) {
        let char = strs[0][i];
        
        for (let j = 1; j < strs.length; j++) {
            if (i >= strs[j].length || strs[j][i] !== char) {
                return strs[0].substring(0, i);
            }
        }
    }
    return strs[0];
};


longestCommonPrefix(["flower","flow","flight"])

