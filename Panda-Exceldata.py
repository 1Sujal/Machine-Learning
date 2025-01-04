import pandas as pd
dataset = "path of file"
df = pd.read_csv(dataset)
seen_countries = set()
country_list = []
country_only = df["Country"]
for country in country_only:
    if country not in seen_countries:
        country_list.append(country)
        seen_countries.add(country)
icountry = input("Name of country you want data of: \n")
max_match_count = 0
best_match_country = ""
if icountry in country_list:
    data = df[df["Country"]==icountry]
    print(f"The usuage of safe drinking water of that country is: {data}")
else:
    for list in country_list:
        len_of_country = len(list)
        len_of_input = len(icountry)
        match_count = 0
        for char, charr in zip(list, icountry):
            if char == charr:
                match_count += 1
        if match_count > max_match_count:
            max_match_count = match_count
            best_match_country = list
    print(f"Did you mean {best_match_country}?")
    data = df[df["Country"]==best_match_country]
    print(f"The usuage of safe drinking water of that country is: {data}")




