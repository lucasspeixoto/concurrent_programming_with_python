import multiprocessing


def calculate(data: int) -> int:
    return data**2


def main():
    pool_size = multiprocessing.cpu_count() * 2  # 8 * 2 -> 16

    print(f"Pool Size: {pool_size}")

    pool = multiprocessing.Pool(processes=pool_size)

    entries = list(range(7))
    outputs = pool.map(calculate, entries)

    print(f"Outputs: {outputs}")

    pool.close()  # Podem fechar pq será mapeado mais nenhuma função
    pool.join()


if __name__ == "__main__":
    main()
