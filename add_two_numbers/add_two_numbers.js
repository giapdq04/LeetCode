
var addTwoNumbers = function(l1, l2) {
	// console.log(typeof l1)
	const reversedl1 = l1.reverse()
	const reversedl2 = l2.reverse()

    const number1 = Number(reversedl1.join(''))
    const number2 = Number(reversedl2.join(''))

    const result = number1 + number2

    const arrayResult = Array.from(String(result), Number)

    let dummyHead = new ListNode()
    let current = dummyHead

    arrayResult.forEach((digit)=>{
        current.next = new ListNode(digit)
        current = current.next
    })

    return dummyHead.next

};

class ListNode{
    constructor(val = 0, next = null){
        this.val = val
        this.next = next
    }
}

addTwoNumbers([2,4,3],[5,6,4])