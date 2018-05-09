def get_longest_palendrome(string):
    string = string.replace('', '^')
    longest = 0
    position = 0
    length = len(string)
    for index in range(length):
        stretch = 0
        for stretch in range(1, min(index + 1, length - index)):
            text = string[index - stretch:index + stretch + 1]
            if text != text[::-1]:
                stretch -= 1
                break
        if stretch > longest:
            longest = stretch
            position = index
    position -= longest
    return string[position:position + (2*longest + 1)].replace('^', '')
print(get_longest_palendrome("amadamaddabananas"))
