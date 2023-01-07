name = input("Your name: ")

check_sum = 0
for n in name:
    check_sum += ord(n)
print(check_sum)

hexadecimal = ""
hex_str = "0123456789abcdef"
while check_sum // 16 > 0:
    hexadecimal = hex_str[check_sum % 16] + hexadecimal
    check_sum = check_sum // 16
hexadecimal = hex_str[check_sum % 16] + hexadecimal
hexadecimal = "#" + "0" * (6 - len(hexadecimal)) + hexadecimal
print(hexadecimal)
