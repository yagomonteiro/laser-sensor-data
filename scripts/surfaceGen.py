import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

# recebe o CSV como parâmetro
if len(sys.argv) < 2:
    print("Uso: python plot_laser.py <arquivo.csv>")
    sys.exit(1)

csv_file = sys.argv[1]

# carrega dados
data = np.loadtxt(csv_file, delimiter="\t")

# parâmetros
num_beams = data.shape[1]
angles = np.linspace(-np.pi/4, np.pi/4, num_beams)  # feixe ±45°
spacing = 5  # 5 cm entre varreduras no eixo x

# listas para nuvem de pontos
xs, ys, zs = [], [], []

# gera pontos
for t, scan in enumerate(data):
    for i, dist in enumerate(scan):
        if dist > 0:
            x = t * spacing                     # amostra → tempo/posição
            y = dist * np.sin(angles[i])        # lateral
            z = dist * np.cos(angles[i])        # frente
            xs.append(x)
            ys.append(y)
            zs.append(z)

# converte para numpy
xs, ys, zs = np.array(xs), np.array(ys), np.array(zs)

# plota
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# força proporção dos eixos: X mais esticado
ax.set_box_aspect([5, 1, 1])  # aumenta X em relação a Y e Z

p = ax.scatter(xs, ys, zs, c=zs, cmap="viridis", s=2)

ax.set_xlabel("Amostra (x)")
ax.set_ylabel("Lateral (y) [m]")
ax.set_zlabel("Frente (z) [m]")
ax.set_title("Nuvem de pontos do Laser Scanner")

fig.colorbar(p, ax=ax, label="Distância (m)")
plt.show()
