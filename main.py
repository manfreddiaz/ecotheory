import itertools
import multiprocessing
import tasks

from algorithms.reinforce import main as reinforce
from algorithms.dqn import main as dqn


def main(num_seeds=3):
    environments = tasks.load()
    seeds = range(num_seeds)

    with multiprocessing.Pool() as p:
        for alg in [reinforce, dqn]:
            for env, seed in itertools.product(environments, seeds):
                p.apply_async(alg, args=(env, seed))

    p.close()
    p.join()


if __name__ == '__main__':
    main()
