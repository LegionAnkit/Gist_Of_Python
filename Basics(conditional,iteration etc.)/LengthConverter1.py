print("Enter the length in metre")
metre=input()
kms=float(metre)/1000
miles=kms/1.609
roundkms=round(kms,2)
roundmiles=round(miles,2)
print(f"{metre}m is equal to {roundkms}km and {roundmiles}mi")