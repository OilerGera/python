def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)
something = input('Введите текст: ')
something = something.lower()
forbidden=('»','«', ' ','.','?','!',':',';','-',)
for symbol in forbidden:
    if symbol in something:
        something = something.replace(symbol, '')

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")