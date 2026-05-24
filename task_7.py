import random
import matplotlib.pyplot as plt

def monte_carlo_dice(num_rolls=1000000):
    """Імітує кидки двох кубиків та рахує ймовірності."""
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sums_count[dice1 + dice2] += 1
        
    probabilities = {k: (v / num_rolls) * 100 for k, v in sums_count.items()}
    return probabilities

def display_results(mc_probs):
    """Виводить таблицю порівняння та малює графік."""
    # Аналітичні ймовірності з умови
    analytical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    print(f"{'Сума':<10} | {'Монте-Карло (%)':<20} | {'Аналітична (%)':<20}")
    print("-" * 55)
    for s in range(2, 13):
        print(f"{s:<10} | {mc_probs[s]:<20.2f} | {analytical_probs[s]:<20.2f}")
        
    # Графік
    sums = list(range(2, 13))
    mc_values = [mc_probs[s] for s in sums]
    an_values = [analytical_probs[s] for s in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_values, width=0.4, label='Монте-Карло', align='center', color='skyblue')
    plt.bar([s + 0.4 for s in sums], an_values, width=0.4, label='Аналітична', align='center', color='orange')
    plt.xticks(sums)
    plt.xlabel("Сума двох кубиків")
    plt.ylabel("Ймовірність (%)")
    plt.title("Порівняння ймовірностей: Монте-Карло vs Аналітичні")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# --- Тестування Завдання 7 ---
if __name__ == "__main__":
    mc_results = monte_carlo_dice(1000000)
    display_results(mc_results)
