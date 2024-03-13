# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Main code to prompt user input and display the final price
if __name__ == "__main__":
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(original_price, discount_percentage)
        print(f"The final price after applying discount is: ${final_price:.2f}")
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")
