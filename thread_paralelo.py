import threading
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Array ordenado:", arr)
    global count
    count -= 1

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    print("Fatorial de", n, "é:", fatorial(n))
    global count
    count -= 1

def multiplicar_matrizes(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    print("Matriz resultante:", C)
    global count
    count -= 1

def somar_matrizes(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    print("Matriz resultante:", C)
    global count
    count -= 1

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    print("7 é um número primo.")
    global count
    count -= 1

arr = [random.randint(1, 100) for _ in range(10)]
num_fatorial = random.randint(1, 10)
A = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
B = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
num_primo = random.randint(1, 100)

global count
count = 5

thread_bubble_sort = threading.Thread(target=bubble_sort, args=(arr,))
thread_fatorial = threading.Thread(target=fatorial, args=(num_fatorial,))
thread_multiplicar_matrizes = threading.Thread(target=multiplicar_matrizes, args=(A, B))
thread_somar_matrizes = threading.Thread(target=somar_matrizes, args=(A, B))
thread_eh_primo = threading.Thread(target=eh_primo, args=(num_primo,))

thread_bubble_sort.start()
thread_fatorial.start()
thread_multiplicar_matrizes.start()
thread_somar_matrizes.start()
thread_eh_primo.start()

while count > 0:
    pass

print("Todas as funções terminaram.")
