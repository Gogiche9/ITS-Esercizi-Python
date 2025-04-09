pizze = ["Marinara", "Margherita", "Patate"] 

friends_pizzas = pizze.copy()

pizze.append("Halloween")
friends_pizzas.append("Tirolese")
print(f"{pizze}\n{friends_pizzas}")

for i in pizze:
    print(f"I really like {i} pizza")

for e in friends_pizzas:
    print(f"My freind really loves {e} pizzas")
    
pizze.pop()
friends_pizzas.pop(0)

print(f"{pizze}\n{friends_pizzas}")