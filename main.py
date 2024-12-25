from src.input_data import load_reservoir_data
from src.simulation import run_simulation
from src.visualization import visualize_results
from src.export_data import export_to_csv

def main():
    # 1. Load data reservoir
    file_path = "data/reservoir_data.csv"
    data = load_reservoir_data(file_path)
    if data is None:
        return
    
    # 2. Run simulation
    simulated_data = run_simulation(data)
    print(simulated_data)

    # 3. Visualize results
    visualize_results(simulated_data)

    # 4. Export results
    export_path = "data/simulation_results.csv"
    export_to_csv(simulated_data, export_path)

if __name__ == "__main__":
    main()
