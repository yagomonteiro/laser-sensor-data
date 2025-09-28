import numpy as np
import sys

def save_ply(csv_file, ply_file, fov_deg=90, spacing=0.01):
    # Carrega CSV (tab separado)
    data = np.loadtxt(csv_file, delimiter="\t")
    num_scans, num_beams = data.shape
    
    # Ângulos dos feixes
    fov = np.deg2rad(fov_deg)
    angles = np.linspace(-fov/2, fov/2, num_beams)

    points = []

    for t in range(num_scans):
        for j in range(num_beams):
            d = data[t, j]
            if d > 0:  # ignora leituras inválidas
                x = t * spacing
                y = d * np.sin(angles[j])   # lateral
                z = d * np.cos(angles[j])   # frente
                points.append((x, y, z))
    
    points = np.array(points)

    # Salva como PLY (formato ASCII simples)
    with open(ply_file, "w") as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write(f"element vertex {len(points)}\n")
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("end_header\n")
        for p in points:
            f.write(f"{p[0]} {p[1]} {p[2]}\n")

    print(f"PLY salvo em {ply_file} com {len(points)} pontos.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python gera_ply.py entrada.csv saida.ply")
    else:
        save_ply(sys.argv[1], sys.argv[2])
