"""Является ли str1 подпоследовательностью str2? Решить с помозью указателей"""


def is_subsequence(str1, str2):
    chr1 = chr2 = 0
    while chr1 < len(str1) and chr2 < len(str2):
        if str1[chr1] == str2[chr2]:
            chr1 += 1
        chr2 += 1

    if chr1 == len(str1):
        return True
    return False

str1 = "ahbg"
str2 = "ahbgdc"

print(is_subsequence(str1, str2))  # True