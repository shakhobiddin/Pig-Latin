#Take the users input
words = input("Enter your sentence to translate to pig latin: ")
print ("You entered: ", words)

#Now I need to break apart the words into a list
words = words.split(' ')

#Now words is a list, so I can take each one using a loop

k=""
for i in words:
    if len(i) >=0 :
        i = i + "%say" % (i[0].lower())
        i = i[1:]
        k+=str(i)+" "

    else:
        print ("empty")
print(k)
