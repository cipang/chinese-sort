from random import shuffle
import sortfunc


original = [
    "ABC",
    "XYZ",
    "750 Bytes",
    "蔣金俊",
    "杜隆舜",
    "譚衡怡",
    "洪三",
    "洪三郎",
    "一二三",
    "一二三四",
    "彭定康",
    "曾蔭權",
    "張由行",
    "張浩天",
    "舒琪",
]


shuffle(original)
print("Original: " + repr(original))
print("Sorted  : " + repr(sorted(original, key=sortfunc.chinese_sort_key)))
