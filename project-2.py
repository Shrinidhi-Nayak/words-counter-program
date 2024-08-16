def count_words(text):
    
    text = text.strip()
    
    words = text.split()
    
    return len(words)


text = input("Enter your text: ")
    
 
word_count = count_words(text)
    
    
print(f"The number of words in the given text is: {word_count}")