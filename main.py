import itertools
import multiprocessing
import tasks

from algorithms.reinforce import reinforce
from algorithms.dqn import dqn


def main(num_seeds=1):
    environments = tasks.load()
    seeds = range(num_seeds)

    p = multiprocessing.Pool()
    futures = []
    for alg in [reinforce, dqn]:
        for env, seed in itertools.product(environments, seeds):
            futures.append(
                p.apply(alg, args=(env, seed, f"{env}-{alg.__name__}-{seed}"))
            )

    for future in futures:
        future.get()

    p.join()


if __name__ == '__main__':
    main()
