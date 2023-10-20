words = input().split()
words_below = [word for word in words if len(word) % 2 == 0]
print('\n'.join(words_below))