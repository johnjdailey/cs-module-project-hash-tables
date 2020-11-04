#word_count.py



def word_count(s):
    dictionary = {}
    ignoreChars = '" : ; , . - + = / \\ | [ ] { } ( ) * ^ &'.split()
    lower_s = s.lower()
    for i in ignoreChars:
        lower_s = lower_s.replace(i, " ")
    for word in lower_s.split():
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
