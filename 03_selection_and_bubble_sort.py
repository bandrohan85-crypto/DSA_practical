salaries = [45000.75, 52000.0, 39000.3, 61000.8, 47000.25, 88000.0,
    73000.45, 59000.1]

def selection_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
    return sorted_arr

def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

def display_top_5(salary_list):
    top_5 = salary_list[-5:][::-1]
    print("Top 5 Highest Salaries:")
    for i, salary in enumerate(top_5, 1):
        print(f"{i}. ₹{salary:.2f}")

print("Original Salaries:")
print(salaries)
sel_sorted = selection_sort(salaries)
print("\nSalaries Sorted (Selection Sort):")
print(sel_sorted)
display_top_5(sel_sorted)
bub_sorted = bubble_sort(salaries)
print("\nSalaries Sorted (Bubble Sort):")
print(bub_sorted)
display_top_5(bub_sorted)
