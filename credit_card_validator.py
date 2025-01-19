card_num = input("Enter your credit card number : ")
card_num =card_num.replace("-","")
card_num =card_num.replace(" ","")
card_num =card_num[::-1]

sum_odd_digits =0
sum_even_digits =0
total=0
for digit in card_num[::2]:
    sum_odd_digits += int(digit)

for digit in card_num[1::2]:
    digit = int(digit)*2
    if digit >=10:
        sum_even_digits += (1 + (digit%10))
    else:
        sum_even_digits += digit

total =sum_even_digits + sum_odd_digits
if total%10 == 0:
    print("VALID")
else:
    print("INVALID")