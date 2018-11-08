#print("hello")#
alpha = "abcdefghijklmnopqrstuvwxwz"
alpha = list(alpha)

message = "Hello Nico".lower()


offset = 6

def encode(msg, off):
    output_message = ""
    for char in message:
        if (char==' '):
            output_message += ' '
            continue
        ind = alpha.index(char)
        output_message += alpha[(ind + off)%26]
    return output_message

print(encode("It is almost xmas",26))



