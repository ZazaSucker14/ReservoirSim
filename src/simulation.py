def calculate_pressure_drop(permeability, viscosity, flow_rate, length):
    """
    Menghitung penurunan tekanan berdasarkan parameter reservoir.
    """
    try:
        pressure_drop = (flow_rate * viscosity * length) / permeability
        return pressure_drop
    except ZeroDivisionError:
        print("Error: Permeability cannot be zero.")
        return None

def run_simulation(data):
    """
    Menjalankan simulasi fluida untuk setiap baris data.
    """
    results = []
    for _, row in data.iterrows():
        pressure_drop = calculate_pressure_drop(
            row['permeability'],
            row['viscosity'],
            row['flow_rate'],
            row['length']
        )
        results.append(pressure_drop)
    data['pressure_drop'] = results
    return data
