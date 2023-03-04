import gym
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def play_atlantis(env_in):
    # env_in = gym.make("ALE/Atlantis-v5", render_mode="rgb_array")
    env_in.action_space.seed(81)
    observation_in, info_in = env_in.reset(seed=24)

    # Set up the figure and axis for the animation
    global im
    global fig

    fig, ax = plt.subplots()
    im = ax.imshow(observation_in)
    ax.axis('off')

    # Get the initial number of remaining lives
    global lives
    lives = env_in.ale.lives() + 1

    # Initialize the previous number of lives and time
    lives_prev = lives
    global times
    time_start = time.time()
    times = time_start

    # Define a function to update the plot for each frame of the animation
    def update(frame, lives_prev, time_prev, last_life_lost_time):
        # Take a random action and get the next observation and reward
        observation_upt, _, _, info_upt, _ = env.step(env.action_space.sample())
        # observation_upt, reward, done, info_upt = env.step(1)
        # Update the plot with the new observation
        im.set_data(observation_upt)

        # Update the number of remaining lives if it has changed

        lives_upt = env.ale.lives()
        if lives_upt != lives_prev:
            lives_prev = lives_upt

            time_since_last_life_lost = time.time() - last_life_lost_time
            last_life_lost_time = time.time()

            # print("Remaining lives:", lives_upt, "Time since last life lost:", time_since_last_life_lost)
            print("Remaining lives:", lives_upt, ". Time since I've become SMARTER!!! :D ",
                  time_since_last_life_lost, " milliseconds.")

        return im,

    # Create the animation with the update function and 1000 frames
    try:
        ani = FuncAnimation(fig, update, frames=1000, fargs=(lives, times, time_start), blit=True)
        # ani = FuncAnimation(fig, update, frames=1000, blit=True)
        plt.show()
    except Exception as e:
        print(e)

    # Show the animation
    plt.show()
    # print("observation = ", observation, "\ninfo = ", info)
    env_in.close()



def play_mspacman(env_in):
    # use atari env: MsPacman-v4, animate the game as above, record highest score and print out
    env = gym.make("MsPacman-v4", render_mode="rgb_array")
    env.action_space.seed(81)
    observation, info = env.reset(seed=24)


# keyboard input to choose the game: 0: MsPacman, 1: Atlantis, 2: Pong, 3: SpaceInvaders
game = input("Choose the game: 0: MsPacman, 1: Atlantis, 2: Pong, 3: SpaceInvaders ")
if game == "0":
    env = gym.make("MsPacman-v4")
elif game == "1":
    env = gym.make("ALE/Atlantis-v5", render_mode="rgb_array")
    observation, info = env.reset(seed=24)
    play_atlantis(env)

elif game == "2":
    env = gym.make("Pong-v4")
elif game == "3":
    env = gym.make("SpaceInvaders-v0")
else:
    print("Wrong input. Exit.")
    exit(0)

# # use atari env: BankHeist-v4
# env = gym.make("BankHeist-v4")
# env.action_space.seed(42)
#
# observation, info = env.reset(seed=42)
#
# for _ in range(1000):
#     observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
#
#     if terminated or truncated:
#         observation, info = env.reset()
#
# env.close()
#
#
# # use atari env: Pong-v4
# env = gym.make("Pong-v4")
# env.action_space.seed(42)
#
# observation, info = env.reset(seed=42)
#
# for _ in range(1000):
#     observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
#
#     if terminated or truncated:
#         observation, info = env.reset()
#
# env.close()
#
#
# # use atari env: SpaceInvaders-v4
# env = gym.make("SpaceInvaders-v4")
# env.action_space.seed(42)
#
# observation, info = env.reset(seed=42)
#
# for _ in range(1000):
#     observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
#
#     if terminated or truncated:
#         observation, info = env.reset()
#
# env.close()
#
# # use atari env: "ALE/Alien-v5", not render_mode is not "human",
# # give me observation, reward, terminated, truncated, info, in step by step
# # let me know what is the difference between "human" and "rgb_array"
# # print out the observation, reward, terminated, truncated, info
# env = gym.make("ALE/Alien-v5", render_mode="rgb_array")
# env.action_space.seed(42)
#
# observation, info = env.reset(seed=42)
#
# for _ in range(1000):
#     observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
#
#     if terminated or truncated:
#         observation, info = env.reset()
#
# env.close()


# # Define a function to update the plot for each frame of the animation
# def update(frame, lives_prev):
#     # Take a random action and get the next observation and reward
#     observation_upt, _, _, info_upt, _ = env.step(env.action_space.sample())
#     # observation_upt, reward, done, info_upt = env.step(1)
#     # Update the plot with the new observation
#     im.set_data(observation_upt)
#
#     # Update the number of remaining lives if it has changed
#     if env.ale.lives() != lives_prev:
#         lives_upt = env.ale.lives()
#         print("Remaining lives:", lives_upt)
#
#     # Return the updated plot and text
#     return im,
#
#
# # Create the animation with the update function and 1000 frames
# try:
#     ani = FuncAnimation(fig, update, frames=1000, fargs=(lives, ), blit=True)
#     # ani = FuncAnimation(fig, update, frames=1000, blit=True)
#     plt.show()
# except Exception as e:
#     print(e)
#
#
# # Show the animation
# plt.show()
# print("observation = ", observation, "\ninfo = ", info)
# env.close()
#
# # use atari env: MsPacman-v4, animate the game as above, record highest score and print out
# env = gym.make("MsPacman-v4", render_mode="rgb_array")
# env.action_space.seed(81)
# observation, info = env.reset(seed=24)
#
# # Create the animation with the update function and 1000 frames
# try:
#     ani = FuncAnimation(fig, update, frames=1000, fargs=(lives,), blit=True)
#     plt.show()
# except Exception as e:
#     print(e)

