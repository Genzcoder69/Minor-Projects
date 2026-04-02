# First of all we have to take all the inputs
Electricity_Charge_per_unit = int(input("Enter the Electricity Charge per unit :>>>"))
Total_Person = int(input("Enter the No. of Total person living in House :>>>"))
Electricity_Spend = int(input("Enter the monthly Electricity Spend :>>>"))
Rent = int(input("Enter the monthly house rent :>>>"))
Food = int(input("Enter the amount of ordered food :>>>"))

# After taking all the inputs we have to calculate Total electricity charges
Total_Electricity_Bill = Electricity_Spend * Electricity_Charge_per_unit

# Now we have to finally calculate the Total house rent by using formula
Total_House_Rent = (Food + Rent + Total_Electricity_Bill) / Total_Person

# This is the output of total house rent
print(f"Each person will have to pay {Total_House_Rent}")

# Now, take name of Tenants who are living in House
Tenant_name = input("Enter the name of Tenants :>>>").lower().split()
print(f"The name of rent holder's are {Tenant_name}")

# Remove the Tenant who do not want to pay rent
Tenant_remove = input("Enter the name of Tenant who doesn't want to pay rent :>>>").lower()

if Tenant_remove in Tenant_name:
    Tenant_name.remove(Tenant_remove)
    print(f"The {Tenant_remove} has been removed from the House")
    print(f"Remaining Tenants are {Tenant_name}")
else:
    print("Everything is fine")
