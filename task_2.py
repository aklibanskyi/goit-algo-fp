import turtle

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return
    
    # Малюємо стовбур/гілку
    t.forward(length)
    
    # Зберігаємо поточну позицію та кут
    pos = t.position()
    heading = t.heading()
    
    # Ліва гілка
    t.left(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)
    
    # Повертаємось на розгалуження
    t.setposition(pos)
    t.setheading(heading)
    
    # Права гілка
    t.right(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)
    
    # Повертаємось у початкову точку
    t.setposition(pos)
    t.setheading(heading)

def main():
    try:
        level = int(input("Введіть рівень рекурсії для дерева Піфагора (рекомендовано 5-10): "))
    except ValueError:
        print("Некоректне значення, встановлено рівень 6 за замовчуванням.")
        level = 6

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Дерево Піфагора")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90) # Повертаємо черепашку вгору
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.color("brown")
    
    draw_pythagoras_tree(t, 100, level)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
