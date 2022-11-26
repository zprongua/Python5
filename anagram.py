def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    second = list(second_string)
    for x in first_string:
        for j in range(len(second_string)):
            if x == second[j]:
                second.pop(j)
                break
    return len(second) == 0