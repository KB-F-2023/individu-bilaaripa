import heapq

# Generate graph node/kota dan edge beserta cost
graph = {
    'A': {'B': 5, 'D': 9, 'E': 3},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'G': 7},
    'D': {'A': 9, 'F': 4},
    'E': {'A': 3, 'F': 2},
    'F': {'D': 4, 'E': 2, 'G': 6},
    'G': {'C': 7, 'F': 6}
}

# Tentukan start dan goal
start = 'A'
goal = 'F'

# Generate SLD setiap node ke goal
sld = {
    'A': 11,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 3,
    'G': 0
}

def astar(graph, start, goal, sld):
    # Inisialisasi nilai heuristik awal dan jarak sejauh ini dari start ke setiap node
    heuristics = {node: sld[node] for node in graph}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Inisialisasi priority queue dan masukkan node start
    queue = [(heuristics[start], start)]
    heapq.heapify(queue)

    while queue:
        # Pop node dengan heuristik terkecil dari priority queue
        current_heuristic, current_node = heapq.heappop(queue)

        # Jika node yang di-pop adalah goal, kembalikan jarak sejauh ini
        if current_node == goal:
            return distances[current_node]

        # Loop melalui tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru dari start ke tetangga melalui node saat ini
            distance = distances[current_node] + weight

            # Jika jarak baru lebih kecil dari jarak sejauh ini dari start ke tetangga, update nilai
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Hitung nilai heuristik baru dari tetangga ke goal dan tambahkan dengan jarak sejauh ini
                heuristic = distance + sld[neighbor]
                heuristics[neighbor] = heuristic

                # Masukkan tetangga ke priority queue dengan nilai heuristik baru
                heapq.heappush(queue, (heuristic, neighbor))

    # Jika goal tidak ditemukan, kembalikan None
    return None

# Jalankan algoritma A* dan tampilkan jarak terpendek
distance = astar(graph, start, goal, sld)
if distance:
    print(f"Jarak terpendek dari {start} ke {goal} adalah {distance}")
else:
    print(f"Tidak ada jalur yang menghubungkan {start} dan {goal}")
