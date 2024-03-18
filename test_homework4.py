#Artur Kazukevich
#06.06.2023
#Grodno-IT-Academy-Python
#Homework-4-Test_Suite

import pytest
import homework4 as hw


class TestFibonacci():
    def test_fibonacci_output_type(self):
        assert type(hw.fibonacci(1)) == type(1)
    def test_fib_values(self):
        fib_num_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049]
        for n in range(1,100):
            fib = hw.fibonacci(n)
            assert fib == fib_num_sequence[n - 1]


class TestPalindrome():
    def test_palindrome_output_type(self):
        assert type(hw.palindrome(0)) == type(True)
    def test_palindrome_single_digit(self):
        for i in range(0,10):
            assert hw.palindrome(i) == True
    def test_palindrome_double_digit(self):
        pali_list = [i for i in range(11,100,11)]
        for i in range(10,100):
            if i in pali_list:
                assert hw.palindrome(i) == True
                continue
            assert hw.palindrome(i) == False
    def test_palindrome_triple_digit(self):
        pali_list = []
        for x in range(1,10):
            for y in range(10):
                p = x*101 + y*10
                pali_list.append(p)
        for i in range(100,1000):
            if i in pali_list:
                assert hw.palindrome(i) == True
            else:
                assert hw.palindrome(i) == False
    def test_palindrome_quadruple_digit(self):
        pali_list = []
        for x in range(1,10):
            for y in range(10):
                p = x*1001 + y*110
                pali_list.append(p)
        for n in range(1000,10000):
            if n in pali_list:
                assert hw.palindrome(n) == True
            else:
                assert hw.palindrome(n) == False
    def test_palindrome_five_digit(self):
        pali_list = []
        for x in range(1,10):
            for y in range(10):
                for z in range(10):
                    p = x*10001 + y * 1010 + z * 100
                    pali_list.append(p)
        for n in range(10000,100000):
            if n in pali_list:
                assert hw.palindrome(n) == True
            else:
                assert hw.palindrome(n) == False
    #float killer
    def test_palindrome_12345678987654321(self):
        assert hw.palindrome(12345678987654321) == True
        assert hw.palindrome(12345678987754321) == False
        assert hw.palindrome(11345678987654311) == True
        assert hw.palindrome(11345678987754311) == False


class TestFizzBuzz:
    def test_fizz_buzz_type(self):
        #Sample generator for type comparrison
        sample_gen = (_ for _ in range(3))
        #Getting Generator for test
        testing_gen = hw.fizz_buzz(0,2)
        #assertion
        assert type(testing_gen) == type(sample_gen)
    def test_fizz_buzz_1_15(self):
        #Getting Generator for test
        testing_gen = hw.fizz_buzz(1,15)
        #generating output into array
        gen_output = [i for i in testing_gen]
        expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        #assertion
        assert gen_output == expected_output
    def test_fizz_buzz_15_1(self):
        #Getting Generator for test
        testing_gen = hw.fizz_buzz(15,1)
        #generating output into array
        gen_output = [i for i in testing_gen]
        expected_output = ['FizzBuzz', '14', '13', 'Fizz', '11', 'Buzz', 'Fizz', '8', '7', 'Fizz', 'Buzz', '4', 'Fizz', '2', '1']
        #assertion
        assert gen_output == expected_output
    def test_fizz_buzz_100_0(self):
        #Getting Generator for test
        testing_gen = hw.fizz_buzz(100,0)
        #generating output into array
        gen_output = [i for i in testing_gen]
        expected_output = ['Buzz', 'Fizz', '98', '97', 'Fizz', 'Buzz', '94', 'Fizz', '92', '91', 'FizzBuzz', '89', '88', 'Fizz', '86', 'Buzz', 'Fizz', '83', '82', 'Fizz', 'Buzz', '79', 'Fizz', '77', '76', 'FizzBuzz', '74', '73', 'Fizz', '71', 'Buzz', 'Fizz', '68', '67', 'Fizz', 'Buzz', '64', 'Fizz', '62', '61', 'FizzBuzz', '59', '58', 'Fizz', '56', 'Buzz', 'Fizz', '53', '52', 'Fizz', 'Buzz', '49', 'Fizz', '47', '46', 'FizzBuzz', '44', '43', 'Fizz', '41', 'Buzz', 'Fizz', '38', '37', 'Fizz', 'Buzz', '34', 'Fizz', '32', '31', 'FizzBuzz', '29', '28', 'Fizz', '26', 'Buzz', 'Fizz', '23', '22', 'Fizz', 'Buzz', '19', 'Fizz', '17', '16', 'FizzBuzz', '14', '13', 'Fizz', '11', 'Buzz', 'Fizz', '8', '7', 'Fizz', 'Buzz', '4', 'Fizz', '2', '1', 'FizzBuzz']
        #assertion
        assert gen_output == expected_output
    def test_fizz_buzz_0_100(self):
        #Getting Generator for test
        testing_gen = hw.fizz_buzz(0,100)
        #generating output into array
        gen_output = [i for i in testing_gen]
        expected_output = ['FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz', '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73', '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz']
        #assertion
        assert gen_output == expected_output
    def test_fizz_buzz_neg15_15(self):
        #Getting Generator for test
        testing_gen = hw.fizz_buzz(-15,15)
        #generating output into array
        gen_output = [i for i in testing_gen]
        expected_output = ['FizzBuzz', '-14', '-13', 'Fizz', '-11', 'Buzz', 'Fizz', '-8', '-7', 'Fizz', 'Buzz', '-4', 'Fizz', '-2', '-1', 'FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        #assertion
        assert gen_output == expected_output
