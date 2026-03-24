medical_data = """Marina Allison   ,27   ,   31.1 , #7010.0   ;Markus Valdez   ,   30, 22.4,   #4050.0 ;Connie Ballard ,43 ,   25.3 , #12060.0 ;Darnell Weber ,   35   , 20.6   , #7500.0; Sylvie Charles   ,22, 22.1 ,#3022.0   ;   Vinay Padilla,24, 26.9 ,#4620.0 ;Meredith Santiago, 51   , 29.3 ,#16330.0;   Andre Mccarty, 19,22.7 , #2900.0 ; Lorena Hodson ,65, 33.1 , #19370.0; Isaac Vu ,34, 24.8,   #7045.0"""

# 1. Initial Cleaning (Replace # with $)
updated_medical_data = medical_data.replace('#', '$')
medical_data_split = updated_medical_data.split(';')

# 2. Clean and Structure Data (Stripping whitespace and casing)
medical_records_clean = []
for record in medical_data_split:
    item = [info.strip() for info in record.split(',')]
    item[0] = item[0].upper() # Uppercase names for consistency
    medical_records_clean.append(item)

# 3. Create Categorized Lists using List Comprehensions
names = [record[0] for record in medical_records_clean]
ages = [record[1] for record in medical_records_clean]
bmis = [float(record[2]) for record in medical_records_clean]
# Strip '$' and convert to float for math operations
insurance_costs = [float(record[3].replace('$', '')) for record in medical_records_clean]

# 4. Analysis
avg_bmi = sum(bmis) / len(bmis)
avg_cost = sum(insurance_costs) / len(insurance_costs)

print(f"Average BMI: {avg_bmi:.2f}")
print(f"Average Insurance Cost: ${avg_cost:.2f}\n")

# 5. Final Summary Output
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old with a BMI of {bmis[i]} and a cost of ${insurance_costs[i]}.")
