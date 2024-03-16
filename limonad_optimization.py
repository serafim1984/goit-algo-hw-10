import pulp

# Ініціалізація моделі
model = pulp.LpProblem('Maximize Beverage Production', pulp.LpMaximize)

# Змінні
Lemonade = pulp.LpVariable('Lemonade', lowBound = 0, cat = 'Continuous')
Juice = pulp.LpVariable('Juice', lowBound = 0, cat = 'Continuous')

# Обмеження ресурсів
model += 2 * Lemonade + 1 * Juice <= 100 # Вода
model += 1 * Lemonade <= 50 # Цукор
model += 1 * Lemonade <= 30 # Лимонний сік
model += 2 * Juice <= 40 # Фруктове пюре

# Функція максимізації виробництва
model += Lemonade + Juice

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Виробити 'Лимонаду':", Lemonade.varValue)
print("Виробити 'Фруктового соку':", Juice.varValue)
