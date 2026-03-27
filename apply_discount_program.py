def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'

    elif price <= 0:
        return 'The price should be greater than 0'

    
    elif not isinstance(discount, (int, float)):
        return 'The discount should be a number'

   
    elif not (0 <= discount <= 100):
        return 'The discount should be between 0 and 100'

   
    else:
        final_price = price * (1 - discount / 100)
       
        return round(final_price, 2)
