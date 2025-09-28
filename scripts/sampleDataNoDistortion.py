import numpy as np
import matplotlib.pyplot as plt

# Carrega o CSV (substitua pelo seu arquivo)
data = np.loadtxt("data/laser_scans_full.csv", delimiter="\t")

# Pega só as 10 primeiras varreduras
amostras = data[:10, :]

# Calcula os ângulos do feixe (distribuídos no FOV de 90°)
num_colunas = amostras.shape[1]
fov = np.deg2rad(90)  # 90 graus em radianos
angles = np.linspace(-fov/2, fov/2, num_colunas)

plt.figure(figsize=(8,6))

for i, dists in enumerate(amostras):
    # Converte para coordenadas cartesianas
    x = dists * np.cos(angles)   # Frente
    y = dists * np.sin(angles)   # Lateral
    
    # Agora plota invertido (Frente no eixo X, Lateral no eixo Y)
    plt.plot(x, y, label=f"Amostra {i+1}")

# Marca posição do robô
plt.scatter(0, 0, c="red", marker="s", label="Robô")

plt.xlabel("Frente (X) [m]")
plt.ylabel("Lateral (Y) [m]")
plt.title("Primeiras 10 varreduras do laser (corrigido)")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
