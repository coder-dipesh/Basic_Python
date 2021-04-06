'''

Input the weight of a person in either kg or lbs. If the person provides his/her weight in kg then convert it into lbs
else convert it to kg.

'''


raw_weight=float(input("Enter the weight : "))
weight_type=input("Enter the weight type (kg/lbs): ")

if  weight_type=='kg':
    converted_lbs=raw_weight*2.20
    print(f"The weight is {converted_lbs} lbs.")

elif  weight_type=='lbs':
    converted_kg=raw_weight*0.4535
    print(f"The weight is {converted_kg} kg.")

else:
    print(f"Please enter weight type kg or lbs only !!")