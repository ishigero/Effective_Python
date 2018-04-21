# coding: utf-8

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
            


address = 'For score and seven years ago'
result = index_words(address)
result_iter = list(index_words_iter(address))

print(result)        #[0, 4, 10, 14, 20, 26]
print(result_iter)   #[0, 4, 10, 14, 20, 26]
