bill = float(input("Total bill amount?    "))
print("Level of service?")
service = input("Please choose good, fair or bad:   ")
split = int(input("Split how many ways?   "))

if service == "good":
    tip = (bill*0.20)
    total = (bill+tip)

elif service == "fair":
    tip = (bill*0.15)
    total = (bill+tip)

elif service == "bad":
    tip = (bill*0.10)
    total = (bill+tip)

print("tip amount:  "f'${tip:.2f}')
print("total amount:  "f'${total:.2f}')
print("ammount per person:  "f'${total/split:.2f}') 