import multiprocessing


def calculate(data: int) -> int:
    return data**2


def print_process_name() -> None:
    print(f"Starting with the process: {multiprocessing.current_process().name}")


def main():
    pool_size = multiprocessing.cpu_count() * 2  # 8 * 2 -> 16

    print(f"Pool Size: {pool_size}")

    pool = multiprocessing.Pool(
        processes=pool_size, initializer=print_process_name
    )  # initializer -> Função executada para cada processo criado

    entries = list(range(7))
    outputs = pool.map(calculate, entries)

    print(f"Outputs: {outputs}")

    pool.close()  # Podem fechar porque não será mapeado mais nenhuma função
    pool.join()


if __name__ == "__main__":
    main()
