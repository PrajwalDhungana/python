print('*************** TIPS *************')
print(":) = đ")
print(":( = âšī¸")
print(":_( = đĸ")
print("")
message = input(">>")

def emojiConverter(message):
    emojis = {
        ":)": "đ",
        ":(": "âšī¸",
        ":_(": "đĸ",
    }

    output = ""
    words = message.split(' ')
    for word in words:
        output += emojis.get(word, word) + " "

    print(output)

emojiConverter(message)

