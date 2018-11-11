class Palindrome:

    def isPalindrome(self, word: str):
        start = 0;
        end = len(word) - 1;

        if word == '-1':
            return '-1'
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1

        return True

if __name__ == '__main__':
    test = Palindrome();


    while True:
        test_word = input(
            "please enter a string to test  whether it is a palindrome. (enter [-1] to quit stock system)")
        if test_word == '':
            print('string cannot be empty, please re-enter a string')
            continue

        if test.isPalindrome(test_word) == '-1':
            print('Testing end, bye')
            break

        if test.isPalindrome(test_word):
            print(test_word + ' is a palindrome')
        else: print(test_word + ' is not a palindrome')