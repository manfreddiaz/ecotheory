import itertools
import json
import os
import gym

EARTH_GRAVITY = 9.8
GYM_PARAMETERS = {
    "cartpole": {
        "max_episode_steps": 200,
        "reward_threshold": 195.0
    },
    "mountaincar": {
        "max_episode_steps": 200,
        "reward_threshold": -110.0,
    },
    "pendulum": {
        "max_episode_steps": 200
    },
    "acrobot": {
        "reward_threshold": -100.0,
        "max_episode_steps": 500,
    },
    "lander": {
        "max_episode_steps": 1000,
        "reward_threshold": 200
    }
}


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
        kwargs = {
            'gravity': gravity[body] * EARTH_GRAVITY
        }
        gym.register(
            id=env_name,
            entry_point=f"tasks.envs:{tasks[name]}Env",
            kwargs=kwargs,
            **GYM_PARAMETERS[name]
        )
        registry.append(env_name)

    return registry
