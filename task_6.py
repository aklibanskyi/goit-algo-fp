items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    """Вибирає страви, максимізуючи співвідношення калорій до вартості."""
    # Сортуємо за співвідношенням калорії/вартість за спаданням
    sorted_items = sorted(
        items.items(), 
        key=lambda x: x[1]['calories'] / x[1]['cost'], 
        reverse=True
    )
    
    chosen_items = []
    total_calories = 0
    total_cost = 0
    
    for item_name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            chosen_items.append(item_name)
            total_cost += data['cost']
            total_calories += data['calories']
            
    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    """Обчислює оптимальний набір страв (0/1 Knapsack problem)."""
    item_names = list(items.keys())
    n = len(item_names)
    
    # dp[i][w] - макс калорії для перших i предметів з бюджетом w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        cal = items[name]['calories']
        
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(cal + dp[i - 1][w - cost], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
                
    # Відновлення вибраних предметів
    res_calories = dp[n][budget]
    w = budget
    chosen_items = []
    
    for i in range(n, 0, -1):
        if res_calories <= 0:
            break
        # Якщо результат прийшов не зверху, значить предмет був взятий
        if res_calories != dp[i - 1][w]:
            name = item_names[i - 1]
            chosen_items.append(name)
            res_calories -= items[name]['calories']
            w -= items[name]['cost']
            
    return chosen_items, dp[n][budget]

# --- Тестування Завдання 6 ---
if __name__ == "__main__":
    budget = 100
    
    print(f"Бюджет: {budget}")
    greedy_res, g_cal, g_cost = greedy_algorithm(items, budget)
    print(f"Жадібний алгоритм: {greedy_res} | Калорії: {g_cal} | Витрачено: {g_cost}")
    
    dp_res, dp_cal = dynamic_programming(items, budget)
    # Знайдемо витрати для DP результату
    dp_cost = sum(items[item]['cost'] for item in dp_res)
    print(f"Динамічне програмування: {dp_res} | Калорії: {dp_cal} | Витрачено: {dp_cost}")
