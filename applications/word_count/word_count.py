def word_count(s):
    # Your code here
    word_dict = {}
    size = len(s)
    words = s.split(' ')
    count = ""

    if size < 1:
        return {}
    
    for word in words:
        count += word
        if word_dict.get(count):
            word_dict[count] += 1
            
        elif count != "":
            word_dict[word] = 1 
            
        count = ""
    
    return word_dict
            


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))