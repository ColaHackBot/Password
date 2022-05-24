import random
lower_case = "abcdefghijklmnopqrstuvwxyz" 
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789" 
symbol = "#$%&'()*+,-./:;<=>?@![\]^_`{|}~"

ans = lower_case + upper_case + num + symbol

length = 25
password = "".join(random.sample(ans,length))
print("\n\nสร้างรหัสผ่าน 25 หลักเรียบร้อยแล้ว\n\n\nรหัสที่สร้างคือ : ",password,"\n\n")
