#Aura Nayla Djokja_F55123043
# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively split and sort the halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        # Merge the halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Data
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Merge Sort Execution
X_merge = X.copy()
merge_sort(X_merge)
print("Merge Sort Result:", X_merge)

# Quick Sort Execution
X_quick = quick_sort(X.copy())
print("Quick Sort Result:", X_quick)

#Analisis
# 1. Merge Sort
# a. Best Case:
#     Merge Sort tidak bergantung pada urutan awal data.
#     Kompleksitas waktu tetap O(n log n), karena setiap pembagian array menjadi dua dan penggabungan memerlukan waktu konstan relatif.
# b. Worst Case:
#     Sama seperti best case, Merge Sort memiliki kompleksitas O(n log n) untuk semua skenario karena pembagian selalu dilakukan merata, tanpa mempertimbangkan urutan awal.
# c. Average Case:
#     Rata-rata waktu eksekusi juga tetap O(n log n), karena sifat rekursif dan pembagian/penggabungan yang seragam.

# 2. Quick Sort
# a. Best Case:
#     Terjadi jika pivot selalu membagi array menjadi dua bagian yang seimbang. Kompleksitas waktu adalah O(n log n).
# b. Worst Case:
#     Terjadi jika pivot selalu menjadi elemen terkecil atau terbesar, sehingga hanya satu elemen terpisah dari array pada setiap iterasi. Kompleksitas waktu adalah O(n²).
# c. Average Case:
#     Rata-rata, pembagian array cukup seimbang, menghasilkan kompleksitas waktu O(n log n).
