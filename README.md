# TUGAS INDIVIDU
- Nama    : Salsabila Fatma Aripa
- NRP     : 5025211057
- Kelas   : KB-F

## Tugas Individu 1
#### Deskripsi Soal
Buat implementasi program algoritma informed search A* pada kasus pencarian jarak terpendek dari 2 node/kota. Generate graph node/kota dan edge beserta cost, Tentukan start dan goal dan generate SLD setiap node ke goal, dan selesaikan dengan A*

## Algoritma A*
Pencarian A* (A-star) adalah algoritma pencarian yang digunakan untuk mencari jalur terpendek atau solusi terbaik dari suatu masalah, dengan mempertimbangkan biaya atau jarak yang ditempuh serta estimasi biaya atau jarak yang tersisa. Rumus umum untuk algoritma pencarian A* adalah sebagai berikut: 
##### f(n) = g(n) + h(n)
dimana: 
f(n) : adalah nilai total biaya atau jarak dari simpul awal ke simpul tujuan.
g(n) : adalah biaya aktual yang telah ditempuh dari simpul awal  ke simpul n. 
h(n)  : adalah heuristik yang memberikan perkiraan biaya atau jarak tersisa dari simpul n ke simpul tujuan.

Lalu didapatkan penyelesaian sebagai berikut :
- Membuat graph node/kota dan edge beserta cost
- Menentukan Start dan Goal
- Generate SLD setiap node ke goal
- Mengimplementasikan algoritma A* untuk mencari jalur terpendek
- Menerapkan algoritma A* pada graf

## Implementasi Code

Generate graph node/kota dan edge beserta cost:

```sh
graph = {
    'A': {'B': 5, 'D': 9, 'E': 3},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'G': 7},
    'D': {'A': 9, 'F': 4},
    'E': {'A': 3, 'F': 2},
    'F': {'D': 4, 'E': 2, 'G': 6},
    'G': {'C': 7, 'F': 6}
}
```

Tentukan start dan goal:

```sh
start = 'A'
goal = 'F'
```
Tentukan start dan goal:

```sh
start = 'A'
goal = 'F'
```
Generate SLD setiap node ke goal:

```sh
sld = {
    'A': 11,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 3,
    'G': 0
}
```
```sh
def astar(graph, start, goal, sld):
```
Inisialisasi nilai heuristik awal dan jarak sejauh ini dari start ke setiap node:

```sh
heuristics = {node: sld[node] for node in graph}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

```
Inisialisasi priority queue dan masukkan node start:

```sh
    queue = [(heuristics[start], start)]
    heapq.heapify(queue)

    while queue:
```
Pop node dengan heuristik terkecil dari priority queue:

```sh
current_heuristic, current_node = heapq.heappop(queue)'
```
Jika node yang di-pop adalah goal, kembalikan jarak sejauh ini:

```sh
if current_node == goal:
            return distances[current_node]
```
Loop melalui tetangga dari node saat ini:

```sh
for neighbor, weight in graph[current_node].items():
```
Hitung jarak baru dari start ke tetangga melalui node saat ini:

```sh
distance = distances[current_node] + weight
```
Jika jarak baru lebih kecil dari jarak sejauh ini dari start ke tetangga, update nilai:

```sh
if distance < distances[neighbor]:
                distances[neighbor] = distance
```
Hitung nilai heuristik baru dari tetangga ke goal dan tambahkan dengan jarak sejauh ini:

```sh
heuristic = distance + sld[neighbor]
                heuristics[neighbor] = heuristic
```
Masukkan tetangga ke priority queue dengan nilai heuristik baru:

```sh
heapq.heappush(queue, (heuristic, neighbor))
```
Jika goal tidak ditemukan, kembalikan None:

```sh
 return None
```
Jalankan algoritma A* dan tampilkan jarak terpendek:

```sh
distance = astar(graph, start, goal, sld)
if distance:
    print(f"Jarak terpendek dari {start} ke {goal} adalah {distance}")
else:
    print(f"Tidak ada jalur yang menghubungkan {start} dan {goal}")
```
Maka Didapatkan Hasil:

```sh
Jarak terpendek dari A ke F adalah 5
```
