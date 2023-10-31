import concurrent.futures
import multiprocessing


def worker(n):
    core_name = multiprocessing.current_process().name
    print(f'{core_name}: обработка данных => {n}')
    print(f'{core_name}: обработка закончена => {n}')


def summary(a):
    s = []
    final = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        wait_complete = []
        for task in a:
            row = 0
            executor.submit(worker, task)
            # Здесь task - строка матрицы
            wait_complete.append(task)
            for i in task:
                row += i
            s.append(row)
    for i in s:
        final += i
    print(final)


def main():
    print("Enter size of square matrix: \n")
    a = int(input())
    b = [[0] * a for _ in range(a)]
    print(f"Enter {a} rows with {a} elems: \n")
    for i in range(a):
        for j in range(a):
            b[i][j] = int(input())
    print(b)
    summary(b)


if __name__ == '__main__':
    main()
