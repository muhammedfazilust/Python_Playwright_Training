def calculate_bill(price, quantity):
    total =  price*quantity
    if total> 2000:
        discount = total*0.10
        final_amt = total - discount
    return final_amt

result = calculate_bill(500,5)
print(result)