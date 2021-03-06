#print("hello")#
alpha = "abcdefghijklmnopqrstuvwxyz"
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

def decode(msg, off):
    output_message = ""
    msg = msg.lower()
    for char in msg:
        if char not in alpha:
            output_message += char 
            continue
        ind = alpha.index(char)
        output_message += alpha[(ind - off)%26]
    return output_message

def outcomes(msg):
    for offset in range(0, 27):
        print(decode(msg, offset))

if __name__ == "__main__":
    encoded = encode("nico is a goofball", 6);
    outcomes(encoded)
