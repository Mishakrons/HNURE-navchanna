apples = int(input("How many apples do you want?"))
bananas = int(input("How many bananas do you want?"))
orange = int(input("How many oranges do you want?"))
apple_cost = 17
banana_cost = 25
orange_cost = 30
result_apples = (apple_cost*apples) 
print("apples cost:", result_apples)
result_bananas = (banana_cost*bananas)
print("bananas costs:", result_bananas)
result_oranges = (orange_cost*orange)
print("oranges costs:", result_oranges)
result = result_apples + result_bananas + result_oranges
print("all costs:",result)