travel_log = [ #Start of list
{ #start of dictionary 1
    "country": "France",
    "total_visits":12,
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
},
    

{ #start of dictionary 2
    "country": "Germany",
    "total_visits":3,
    "cities_visited" : ["Berlin", "Hamburg"], 
},
]
# todo add function to add new countries

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {} #create new dictionary
    new_country["country"] = country_visited #[key] then = data to be passed
    new_country["visits"] = times_visited #[key] then = data to be passed
    new_country["cities"] = cities_visited #[key] then = data to be passed
    # print(new_country) #Bug test to see new_country
    travel_log.append(new_country) # append the original list travel_log with the new dictionary of new_country 

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)