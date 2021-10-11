counties = ["Araphoe","Denver","Jefferson"]
for county in counties:
    print(county)
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not in the list of counties.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")
    print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters} registered voters.")



#x = 0
#while x <= 3:
    #print(x)
    #x = x + 1


#temperature = int(input("what is the temperature outside? "))

#if temperature > 80:
    #print("Turn on the AC.")
#else:
    #print("Open the window.")
