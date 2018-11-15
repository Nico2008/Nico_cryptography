#print("hello")#
alpha = "abcdefghijklmnopqrstuvwxwz"
alpha = list(alpha)

def encode(msg, off):
    output_message = ""
    msg = msg.lower()
    for char in msg:
        if char not in alpha:
            output_message += char 
            continue
        ind = alpha.index(char)
        output_message += alpha[(ind + off)%26]
    return output_message




