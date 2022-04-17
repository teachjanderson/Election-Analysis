counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict['county'])

for key, value in counties_dict.items():
    print(key,value)


for data in range(3):
    data=F"{voting_data[data]['county']} county has {voting_data[data]['registered_voters']} registered voters."
    print(data)

    
