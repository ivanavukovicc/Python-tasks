
def remove_duplicates_and_sort(words):

    unique_words = sorted(set(words))	
    return unique_words

if __name__ == "__main__":
    
    user_input = input("Unesite neke reci: ")
    input_words = user_input.split()
    result = remove_duplicates_and_sort(input_words)
    print(" ".join(result))
