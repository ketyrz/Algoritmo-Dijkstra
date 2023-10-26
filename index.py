import heapq

def criar_grafo_manual():
    grafo = {
        'A': {'B': 2, 'C': 1},
        'B': {'A': 2},
        'C': {'A': 1, 'M': 7, 'D': 4},
        'D': {'C': 4, 'E': 3},
        'E': {'F': 1, 'J': 2},
        'F': {'G': 8, 'E': 1},
        'G': {'L': 30, 'T': 20, 'F': 8},
        'H': {'I': 6, 'P': 7},
        'I': {'H': 7, 'J': 9},
        'J': {'E': 20, 'I': 9},
        'K': {'Q': 2},
        'L': {'M': 5, 'G': 30},
        'M': {'L': 5, 'C': 7},
        'N': {'O': 3, 'Q': 5},
        'O': {'N': 3, 'P': 10},
        'P': {'O': 10, 'H': 7},
        'Q': {'R': 4, 'K': 2, 'N': 5, 'T': 5},
        'R': {'Q': 4, 'S': 2},
        'S': {'R': 2, 'T': 10},
        'T': {'S': 10, 'Q': 5, 'G': 20}
    }
    return grafo

def dijkstra(grafo, inicio, fim):
    distancias = {ponto: float('infinity') for ponto in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    predecessores = {}

    while fila_prioridade:
        distancia_atual, ponto_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[ponto_atual]:
            continue

        for vizinho, valor in grafo[ponto_atual].items():
            distancia = distancia_atual + valor

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = ponto_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    # Reconstruindo a rota
    rota = []
    ponto = fim
    while ponto is not None:
        rota.insert(0, ponto)
        ponto = predecessores.get(ponto)

    return distancias[fim], rota

ponto_inicio = 'A'
ponto_fim = 'T'

# Use o grafo manual com os novos valores
grafo = criar_grafo_manual()

menor_distancia, rota = dijkstra(grafo, ponto_inicio, ponto_fim)

print(f'Menor caminho entre o ponto {ponto_inicio} e o ponto {ponto_fim} é de {menor_distancia} unidades de distância.')
print(f'Rota: {rota}')