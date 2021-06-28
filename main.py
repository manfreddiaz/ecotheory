import itertools
import multiprocessing
import tasks

from algorithms.reinforce import reinforce
from algorithms.dqn import dqn


def main(num_seeds=3):
    environments = tasks.load()
    seeds = range(num_seeds)

    futures = []
    p = multiprocessing.Pool()
    for alg in [reinforce, dqn]:
        for env, seed in itertools.product(environments, seeds):
            exp_id = f"{env}-{alg.__name__}-{seed}"
            print(f"[spawning] -> {exp_id}")
            futures.append(
                p.apply_async(alg, args=(env, seed, exp_id))
            )

    for future in futures:
        future.get()

    p.join()


if __name__ == '__main__':
    main()
