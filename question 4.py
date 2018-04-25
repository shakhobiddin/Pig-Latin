pig = 'ay'

sentence= input("Enter a word:")
if len(sentence) > 0 and sentence.isalpha():
    word = sentence.lower()
    a = word[0]
    if a == ('a' or 'e' or 'i' or 'o' or 'u'):
        new_word = word + pig
        print (new_word)
    else:
        new_word = word[1:] + a + pig
        print (new_word)
else:
    print ('empty')
