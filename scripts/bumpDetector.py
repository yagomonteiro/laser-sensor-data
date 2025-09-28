import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def detectar_irregularidades(csv_file, limiar=0.02, janela=11, poly=2):
    # Carrega CSV (tab separado)
    data = np.loadtxt(csv_file, delimiter="\t")
    num_scans, num_beams = data.shape

    # Laterais como referência
    ref = (data[:, 0] + data[:, -1]) / 2
    centro = data[:, num_beams // 2]

    # Diferença entre centro e referência
    diff = centro - ref

    # Suaviza para reduzir ruído
    diff_smooth = savgol_filter(diff, janela, poly)

    # Classificação ponto a ponto
    labels = np.zeros_like(diff_smooth, dtype=int)  # 0 = normal, +1 = vão, -1 = lombada
    labels[diff_smooth > limiar] = 1
    labels[diff_smooth < -limiar] = -1

    return diff, diff_smooth, labels

def plot_result(diff, diff_smooth, labels):
    plt.figure(figsize=(10,6))
    plt.plot(diff, alpha=0.4, label="Original")
    plt.plot(diff_smooth, label="Suavizado", linewidth=2)

    # Marca lombadas e vãos
    idx_lombada = np.where(labels == -1)[0]
    idx_vao = np.where(labels == 1)[0]

    plt.scatter(idx_lombada, diff_smooth[idx_lombada], c="red", label="Lombada")
    plt.scatter(idx_vao, diff_smooth[idx_vao], c="blue", label="Vão")

    plt.title("Detecção de irregularidades")
    plt.xlabel("Amostra (linha no tempo)")
    plt.ylabel("Desvio centro–referência [m]")
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------
# Exemplo de uso:
csv_file = "data/laser_scans_full.csv"
diff, diff_smooth, labels = detectar_irregularidades(csv_file, limiar=0.02)
plot_result(diff, diff_smooth, labels)
