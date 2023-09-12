def count_upper_lower(sentence):

    upper = 0	
    lower = 0

    for i in sentence:
        if i.isupper():
            upper += 1

        elif i.islower():
            lower += 1

    return upper, lower

if __name__ == "__main__":

    user_input = input("Unesite neku recenicu: ")
    upper, lower = count_upper_lower(user_input)
    print(f"UPPER CASE {upper} LOWER CASE {lower}")
