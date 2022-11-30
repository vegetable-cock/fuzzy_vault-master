degree=4
word = "ddudhgahdoighoaisgho"
word = word.upper() #把字符串word中的小写字符转换成大写
n = len(word) // degree # n为系数的长度
if n < 1: n = 1 #如果n<1就拉到1
    #substrings = [word[i:i + n] for i in range(0, len(word), n)]  #用以下两句代替
rang = list(range(0, len(word), n))
substrings = [word[i:i + n] for i in rang] 

coeffs = []
for substr in substrings:
    num = 0
    for x, char in enumerate(substr):
        num += ord(char) * 100**x
    coeffs.append(num**(1/3.0))
print(coeffs)

x= '''the x is what??'''
y = 0
degreee = len(coeffs) - 1

for coeff in coeffs:
    y += x**degreee * coeff  # y=cx^4+cx^3+cx^2+cx
    degreee -= 1
    
print(y)