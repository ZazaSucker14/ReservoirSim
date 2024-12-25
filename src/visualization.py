import matplotlib.pyplot as plt

def visualize_results(data):
    """
    Visualize pressure drop results using a line chart.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['pressure_drop'], marker='o', linestyle='-', color='b')
    plt.title("Reservoir Fluid Simulation Results")
    plt.xlabel("Simulation Index")
    plt.ylabel("Pressure Drop (unit)")
    plt.grid(True)
    plt.show()
