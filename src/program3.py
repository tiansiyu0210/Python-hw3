class CreditCard:

    def main(self):
        number = input('please input your credit number. (enter [-1] to quit stock system)')
        if number == '-1':
            print('Quit')
            return False
        if not self.isValid(number):
            print(number + " is not a valid credit card number")
        else:print(number + " is a valid credit card number")

        return True


    def isValid(self, numbers: str) -> bool:
        if len(numbers) < 13 or len(numbers) > 16:
            return False
        if not numbers.startswith('4') and not numbers.startswith('5') and not numbers.startswith('6') and not numbers.startswith('37'):
            return False

        print(self.sumOfDoubleEvenPlace(numbers) + self.sumOfOddPlace(numbers))
        a, b = divmod(self.sumOfDoubleEvenPlace(numbers) + self.sumOfOddPlace(numbers), 10)

        if b != 0:
            return False

        return True

    def sumOfDoubleEvenPlace(self, number: str) -> int:
        start = 1;
        end = len(number) - 1;
        sum = 0;
        while start <= end:
            sum = sum + int(number[start])
            start = start + 2

        return sum;

    def sumOfOddPlace(self, number: str) -> int:
        start = 0;
        end = len(number) - 1;
        sum = 0;
        while start <= end:
            sum = sum + self.getDigit(number[start])
            start = start + 2

        return sum

    def getDigit(self, number: str) -> int:
        result = int(number)*2;

        if  result <= 9:
            return result;
        else:
            a, b = divmod(result, 10)
            return a + b

if __name__ == '__main__':

    test = CreditCard()

    while True:
        if not test.main():
            break;