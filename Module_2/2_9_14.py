def filter_anagrams(word: str, words: list):
    return list(
        filter(
            lambda x: sorted(x) == sorted(word),
            words
        )
    )

print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))