import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pickle

directory = "C:/Users/kople/Documents/Personal Git repos/mizzou_ea_project1/results/final_populations"
func = 'rosenbrock'
# Save the array with Pickle
with open(f'{directory}/{func}-2211.pkl', 'rb') as f:
    populations = pickle.load(f)


# Define the Rosenbrock function
def rosenbrock(x, y):
    return (y-x**2)**2 + (1-x)**2

# Randomly select 9 generations, including the 2nd and last generations
selected_generations = [1, len(populations) - 1] + np.random.choice(range(1, len(populations) - 1), 7, replace=False).tolist()

# Create a list of perspectives for each frame
perspectives = [(45, 45), (30, 60), (60, 30), (90, 0), (0, 90), (45, 135), (135, 45), (45, 0), (0, 45)]

# Create an animated 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Iterate over selected generations and perspectives to generate frames
for i, generation_idx in enumerate(selected_generations):
    population = populations[generation_idx]
    
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-1, 3, 400)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock(X, Y)
    
    ax.plot_surface(X, Y, Z, cmap='viridis')
    
    ax.set_title(f'Generation {generation_idx}')
    ax.view_init(elev=perspectives[i][0], azim=perspectives[i][1])
    
    # Save each frame as an image (you can change the format)
    plt.savefig(f'{func}_generation_{generation_idx}.png')
    # plt.pause(0.1)  # Pause to allow time for saving and displaying

# Close the plot window when done
plt.close()
