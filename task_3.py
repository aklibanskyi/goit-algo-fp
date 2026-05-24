import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Купа зберігає кортежі (відстань, вершина)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдена відстань більша за вже збережену, ігноруємо
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо новий шлях коротший
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# --- Тестування Завдання 3 ---
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for vertex, distance in shortest_paths.items():
        print(f"До {vertex}: {distance}")
