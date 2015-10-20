#!/usr/bin/env python


def find_most_frequent(text):
    str = text.replace(",", " ").replace(".", " ").replace(":", " ").replace(";",
                       " ").replace("!", " ").replace("?", " ").replace("-", " ")
    dict = {}
    result = []

    if str.strip() == "":
        return []

    for word in str.lower().split():
        if not dict.get(word):
            dict[word] = 1
        else:
            dict[word] = dict.get(word) + 1

    max_value = max(dict.values())

    for word, value in dict.items():
        if value == max_value:
            result.append(word)

    result.sort()
    return result

print find_most_frequent("This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.")