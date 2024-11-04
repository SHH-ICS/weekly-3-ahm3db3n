
LARGE_PRICE = 6.00
EXTRA_LARGE_PRICE = 10.00

TOPPING_PRICES = {
    1: 1.00,
    2: 1.75,
    3: 2.50,
    4: 3.35
}

HST_RATE = 0.13


def calculate_pizza_cost(size, toppings):
    if size == 'large':
        base_price = LARGE_PRICE
    elif size == 'extra large':
        base_price = EXTRA_LARGE_PRICE
    else:
        print("Invalid pizza size.")
        return None
    
    topping_cost = TOPPING_PRICES.get(toppings, 0)
    
    subtotal = base_price + topping_cost
    tax = subtotal * HST_RATE
    total = subtotal + tax
    
    return subtotal, tax, total

def main():
    print("Welcome to the Pizza Order System!")
    
    size = input("Enter the pizza size (large/extra large): ").lower()
    if size not in ['large', 'extra large']:
        print("Invalid pizza size. Please try again.")
        return
    
  
    try:
        toppings = int(input("Enter the number of toppings (1-4): "))
        if toppings not in [1, 2, 3, 4]:
            print("Invalid number of toppings. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return
    
  
    subtotal, tax, total = calculate_pizza_cost(size, toppings)
    
    
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax (HST @ 13%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
  
if __name__ == "__main__":
    main()

