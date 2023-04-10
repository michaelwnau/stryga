import pandas as pd

states = ["California", "Oregon", "Washington", "Texas", "New York", "Florida"]
population_millions = [3914, 414, 761, 2871, 1945, 2027]

dict_states = {'States':states, 'Population':population_millions}

df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)
df_states.to_csv('states.csv') # Exporting data to a CSV file

# How would you export your data to a JSON file?
df_states.to_json('states.json') # Exporting data to a JSON file

# You can also use the json library:
# import json
# with open('states.json', 'w') as file:
#     json.dump(dict_states, file)
# print("Data successfully exported to a JSON file!")


#print(states[-4])


# for state in states:
#     if state == "Texas":
#         print(state)
    #print(state)

# with-open-as pattern

# Exporting data to a file in the same directory
# with open('test.txt', 'w') as file:
#     file.write("Data successfully scraped!")

# Using Pandas to export data to a CSV file


    