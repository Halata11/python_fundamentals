words = input().split(', ')
words2 = input().split(',')
my_list = []
for word in words:
    for word2 in words2:
        if word in word2:
            my_list.append(word)
            break


print(my_list)


#60 / 100 wrong code