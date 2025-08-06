
def percentage_liked(ratings):
    """
    計算評分中達到 4 或更高的百分比。

    Args:
        ratings: 一個數字評分列表。

    Returns:
        評分中 >= 4 的比例（浮點數）。
    """
    # 這裡使用生成器表達式以提高記憶體效率。
    # 它計算喜歡的項目總數（其中 True=1, False=0），
    # 而無需創建完整的中間列表。
    return sum(i >= 4 for i in ratings) / len(ratings)

# Do not change: should return 0.5
print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))
