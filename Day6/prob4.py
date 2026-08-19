# Tu ek YouTube creator hai. Ek video ke views (per hour) ek array mein diye hain, sab positive hain. Tujhe janna hai: sabse zyada total views kisi bhi K-consecutive-hours ke stretch mein kitne mile (K ek fixed number hai, jaise "best 3-hour stretch").


def best_k_hour_views(views: list[int], k: int) -> int:
    current_view = sum(views[:k])
    best_view = current_view

    for right in range(k, len(views)):
        current_view += views[right] - views[right - k]
        best_view = max(best_view, current_view)

    return best_view

views = [5, 2, 8, 1, 9, 3]
k = 3

print(best_k_hour_views(views, k))