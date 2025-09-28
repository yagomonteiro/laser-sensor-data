import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python sampleData.py caminho/do/arquivo.csv")
        sys.exit(1)

    csv_file = sys.argv[1]

    # Carrega o CSV
    data = np.loadtxt(csv_file, delimiter="\t")

    # Seleciona as 10 primeiras varreduras
    amostras = data[:10, :]

    plt.figure(figsize=(8, 6))

    for i, dists in enumerate(amostras):
        # Plota diretamente: feixe (índice da coluna) no eixo X e distância no eixo Y
        plt.plot(range(len(dists)), dists, label=f"Amostra {i+1}")

    plt.xlabel("Feixe (coluna)")
    plt.ylabel("Distância [m]")
    plt.title("Primeiras 10 varreduras do laser (sem correção)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
