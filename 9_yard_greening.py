square_metres = float(input())
total_price = square_metres * 7.61
discount = total_price * 0.18
final_price = total_price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")