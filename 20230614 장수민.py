#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

# 학생 30명 정보 생성 함수
def generate_students(n=30):
    students = []
    for _ in range(n):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 두 글자 이름
        age = random.randint(18, 22)  # 나이 18 ~ 22
        score = random.randint(0, 100)  # 성적 0 ~ 100
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬
def selection_sort(arr, key, reverse=False):
    n = len(arr)
    for i in range(n):
        min_max_idx = i
        for j in range(i + 1, n):
            if (arr[j][key] < arr[min_max_idx][key] and not reverse) or (arr[j][key] > arr[min_max_idx][key] and reverse):
                min_max_idx = j
        arr[i], arr[min_max_idx] = arr[min_max_idx], arr[i]

# 삽입 정렬
def insertion_sort(arr, key, reverse=False):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j][key] > key_value[key] and not reverse) or (arr[j][key] < key_value[key] and reverse)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value

# 퀵 정렬
def quick_sort(arr, key, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if (x[key] < pivot[key] and not reverse) or (x[key] > pivot[key] and reverse)]
    greater = [x for x in arr[1:] if (x[key] >= pivot[key] and not reverse) or (x[key] <= pivot[key] and reverse)]
    return quick_sort(less, key, reverse) + [pivot] + quick_sort(greater, key, reverse)

# 계수 정렬
def counting_sort(arr, key, exp, reverse=False):
    output = [0] * len(arr)
    count = [0] * 10
    for student in arr:
        index = student[key] // exp % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        index = arr[i][key] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

# 기수 정렬
def radix_sort(arr, key, reverse=False):
    max_score = max(arr, key=lambda x: x[key])[key]
    exp = 1
    while max_score // exp > 0:
        counting_sort(arr, key, exp, reverse)
        exp *= 10

def print_students(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

def main():
    students = generate_students()
    
    while True:
        print("\n학생 성적 관리 프로그램")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        
        choice = input("메뉴를 선택하세요: ")
        
        if choice == '4':
            print("프로그램을 종료합니다.")
            break
        
        print("\n정렬 전 학생 정보:")
        print_students(students)
        
        sort_key = ''
        if choice == '1':
            sort_key = '이름'
        elif choice == '2':
            sort_key = '나이'
        elif choice == '3':
            sort_key = '성적'
        else:
            print("잘못된 선택입니다.")
            continue
        
        algorithm = input("사용할 정렬 알고리즘을 선택하세요 (1. 선택 정렬, 2. 삽입 정렬, 3. 퀵 정렬, 4. 기수 정렬): ")

        reverse = input("내림차순으로 정렬하시겠습니까? (y/n): ").lower() == 'y'
        
        if algorithm == '1':
            selection_sort(students, sort_key, reverse)
        elif algorithm == '2':
            insertion_sort(students, sort_key, reverse)
        elif algorithm == '3':
            students = quick_sort(students, sort_key, reverse)
        elif algorithm == '4' and sort_key == '성적':
            radix_sort(students, sort_key, reverse)
        else:
            print("잘못된 선택입니다.")
            continue
        
        print("\n정렬 후 학생 정보:")
        print_students(students)

if __name__ == "__main__":
    main()


# In[ ]:




