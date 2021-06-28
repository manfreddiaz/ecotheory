import itertools
import json
import os
import gym

EARTH_GRAVITY = 9.8


def load():
    # (Manfred) Gravity values for each celestial body, relative to Earth gravity
    with open(os.path.join(os.path.dirname(__file__), 'configs/gravity.json'), 'r') as f:
        gravity = json.load(f)

    # (Manfred) Configurable optimal control tasks
    with open(os.path.join(os.path.dirname(__file__), 'configs/tasks.json'), 'r') as f:
        tasks = json.load(f)

    # (Manfred) Create environments for each task on each celestial body
    registry = []
    for body, name in itertools.product(gravity.keys(), tasks.keys()):
        env_name = f"{body}-{tasks[name]}-v0"
        gym.register(
            id=env_name,
            entry_point=f"tasks.envs:{tasks[name]}Env",
            kwargs={
                'gravity': gravity[body] * EARTH_GRAVITY
            }
        )
        registry.append(env_name)

    return registry
