// const sumTwoNumbers = (firstNumber, secondNumber) => {
//     return firstNumber + secondNumber
// }

// const result = sumTwoNumbers(5, 6)
// console.log(result)


// const anotherResult = sumTwoNumbers(8, 7)
// console.log(anotherResult)





// let age = 18

// // garais ifs
// if(age >= 18) {
//   console.log('pilngadīgs')
// } else {
//   console.log('nepilngadīgs')
// }

// // īsais ifs, zināms kā ternary operator
// age >= 18 ? console.log('pilngadīgs') : console.log('nepilngadīgs')




// const reverseNumber = (number) => {
//     const numberToString = number.toString()
//     const stringArray = numberToString.split("")
//     const reversedStringArray = stringArray.reverse()
//     const reversedStringArrayToString = reversedStringArray.join("")
//     const finalStringToNumber = parseInt( reversedStringArrayToString)
//     return finalStringToNumber
// }


// console.log(987, reverseNumber(987))
// console.log(647, reverseNumber(647))
// console.log(69, reverseNumber(69))
// console.log(512, reverseNumber(512))
// console.log(123, reverseNumber(123))


// const vowelCount = (text) => {
//     const allVowels = ["a", "e", "i", "o", "u"]
//     let vowelCount = 0
//     const textToString = text.split("")

//     textToString.forEach((letter) => {
//         const letterIsVowel = allVowels.includes(letter)
//         if(letterIsVowel){
//             vowelCount = vowelCount + 1
//         }
//     });

// return vowelCount

// }

// const result= vowelCount("Pelnam lielo piki")

// console.log(`Vowel count: ${result}`);



// const coinAmountCalculator = (number) => {
//     let currentAmount = number
//     const twoEurCoins = Math.floor(currentAmount / 2)
//     currentAmount = currentAmount - (twoEurCoins * 2)

//     const oneEurCoins = Math.floor(currentAmount / 1)
//     currentAmount= currentAmount - oneEurCoins

//     const halfEurCoins = Math.floor(currentAmount / 0.5)
//     currentAmount= currentAmount - (halfEurCoins * 0.5)



//     console.log(currentAmount)



//    return {
//         "2eur": twoEurCoins,
//         "1eur": oneEurCoins,
//         "50cents": halfEurCoins,
//         "20cents": 0,
//         "10cents": 0,
//         "5cents": 0,
//         "2cents": 0,
//         "1cents": 0,
//       }
// }



const arr = ["a", "b", "a", "c"];

console.log(arr.lastIndexOf("a") + 2);

