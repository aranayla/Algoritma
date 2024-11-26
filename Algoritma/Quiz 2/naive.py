#Aura Nayla Djokja_F55123043
import random

# Set seed untuk memastikan random number sama setiap kali dijalankan
random.seed(40)

# Generate 50 bilangan random dari 0 hingga 100
data = [random.randint(0, 100) for _ in range(50)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Sorting dengan Bubble Sort
sorted_data = bubble_sort(data)
print("Naive Sort (Bubble Sort):")
print("Hasil Sorting:", sorted_data)
