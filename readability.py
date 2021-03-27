from cs50 import get_string


def main():
    s = get_string("Text: ")

    # calculating Coleman-Liau index
    L = (count_letters(s) / count_words(s)) * 100
    S = (count_sentences(s) / count_words(s)) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

# function to count the letters


def count_letters(str):
    total_letters = 0
    for i in range(len(str)):
        if (str[i] >= 'A' and str[i] <= 'Z') or (str[i] >= 'a' and str[i] <= 'z'):
            total_letters += 1
    return total_letters

# function to count words


def count_words(str):
    total_words = 0
    for i in range(len(str)):
        if str[i] == " ":
            total_words += 1
    return total_words + 1


# function to count sentences


def count_sentences(str):
    total_sentences = 0
    for i in range(len(str)):
        if str[i] == '.' or str[i] == '!' or str[i] == '?':
            total_sentences += 1
    return total_sentences


main()