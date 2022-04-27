# Condition: We are in trouble if both monkeys are smiling or if neither of them is smiling. Return TRUE if we are in trouble

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

asmile = False
bsmile = False

print(monkey_trouble(asmile, bsmile))