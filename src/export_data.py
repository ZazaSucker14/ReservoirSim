def export_to_csv(data, output_path):
    """
    Mengekspor data hasil simulasi ke file CSV.
    """
    data.to_csv(output_path, index=False)
    print(f"Results exported to {output_path}")
