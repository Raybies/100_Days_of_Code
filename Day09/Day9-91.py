# Nesting dictionaries
#{key:value}
#{key:[list]}
#{key:{dictionary}}

capitals = {
    "France":"Paris",
}
# Nesting list in a dictionary
travel_log = {
    "France": ["Pairs", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France"  : {"cities_visited" : ["Paris", "Lille", "Dijon" ], "total_visits":[12, 3, 1]}, # dictionary within a dictionary with a list 
}

# Nesting dictionary in a list NOTE: List is accessed by location [0,1,2] while dictionaries are accessed by the key
travel_log = [ #Start of list
    { #start of dictionary 1
        "country": "France",
        "cities_visited" : ["Paris", "Lille", "Dijon" ], 
        "total_visits":12
    },
        
   
    { #start of dictionary 2
        "country": "Germany",
        "cities_visited" : ["Berlin", "Hamburg"], 
        "total_visits":3
    },
]