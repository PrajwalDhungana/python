print('*************** TIPS *************')
print(":) = 🙂")
print(":( = ☹️")
print(":_( = 😢")
print("")
message = input(">>")

def emojiConverter(message):
    emojis = {
        ":)": "🙂",
        ":(": "☹️",
        ":_(": "😢",
    }

    output = ""
    words = message.split(' ')
    for word in words:
        output += emojis.get(word, word) + " "

    print(output)

emojiConverter(message)

