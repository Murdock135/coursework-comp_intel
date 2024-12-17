
import numpy as np
import matplotlib.pyplot as plt
import pickle 

directory = "C:/Users/kople/Documents/Personal Git repos/mizzou_ea_project1/results/final_populations"
func = 'rosenbrock'

# Save the array with Pickle
with open(f'{directory}/{func}-2211.pkl', 'rb') as f:
    populations = pickle.load(f)

# Define the Rosenbrock function
def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

# Create a range of values for the x and y axes
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = rosenbrock(X, Y)


# Define the generations to save
half_gen = len(populations) // 2
last_gen = len(populations) - 1
generations_to_save = [2,3,4,5, half_gen-10,half_gen,half_gen+10 , last_gen-10,last_gen-5]

# Create and save contour plots for selected generations
for generation_index in generations_to_save:
    generation = populations[generation_index]
    x_values = [chromosome[0] for chromosome in generation]
    y_values = [chromosome[1] for chromosome in generation]

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=100, cmap='jet')  # Plot the Rastrigin function contour
    plt.scatter(x_values, y_values, c='red', marker='o', s=10)  # Plot the chromosomes
    plt.title(f'Generation {generation_index}')
    
    # Save the contour plot as an image (adjust the filename as needed)
    plt.savefig(f'{directory}/{func}_contour_plot_generation_{generation_index}.png', dpi=80)
    plt.close()  # Close the current figure to release memory
