pig = 'ay'

sentence= input("Enter a word:")
if len(sentence) > 0 and sentence.isalpha():
    word = sentence.lower()
    a = word[0]
    new_word = word + pig

    new_word = word[1:] + a + pig
    print (new_word)
else:
    print ('empty')
