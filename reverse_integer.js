

var reverse = function(x) {
	var reversedNumber
	if (x < 0) {
		x = Math.abs(x)
		reversedNumber = '-' + x.toString().split('').reverse().join('')
		return parseInt(reversedNumber)
	}

	reversedNumber = x.toString().split('').reverse().join('')

    return parseInt(reversedNumber)
};

console.log(reverse(-123))