import itertools
import multiprocessing
import tasks

from algorithms.reinforce import main as reinforce
from algorithms.dqn import main as dqn


def main(num_seeds=3):
    environments = tasks.load()
    seeds = range(num_seeds)

    futures = []
    p = multiprocessing.Pool()
    for alg in [reinforce, dqn]:
        for env, seed in itertools.product(environments, seeds):
            futures.append(
                p.apply_async(alg, args=(env, seed, f"{env}-{alg.__name__}-{seed}"))
            )

    for future in futures:
        future.wait()



if __name__ == '__main__':
    main()
