# create a hash table of phone digits and letters
# if the digit is empty return empty list
# if the digit is 1 return the value of the digit in the phone hash table
# if the digit is more than 1, return the combination of the first digit values and the rest of the digits
def letterCombinations(digits: str) -> list:
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if not digits:
        return []
    if len(digits) == 1:
        return list(phone[digits])
    else:
        output = []
        for letter in phone[digits[0]]:
            for combination in letterCombinations(digits[1:]):
                output.append(letter + combination)
        return output

digit = input('Enter the digit: ')
print(letterCombinations(digit))
