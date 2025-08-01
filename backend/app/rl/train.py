from stable_baselines3 import PPO
from app.env.warehouse_env import WarehouseEnv

def train():
    env = WarehouseEnv()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("warehouse_ppo")

if __name__ == "__main__":
    train()
