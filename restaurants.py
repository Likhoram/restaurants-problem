def most_varied_visitor(visits):
    #a counter to record how many different restaurants a person went to
    #create a dictionary to store the numbers. key: name of the person. value: count of different restaurants. 
    #loop through input dictionary, each name will be the new dict's key. the key of input dict (restaurant) will be the value of new dict (number of count).
    count_dict = {}
    count = 0
    for name_list in visits.values(): 
        #convert the list to set to get rid of repetitive name in same restaurant
        name_set = set(name_list)
        # print(name_set)
        for name in name_set:
            # if name not in count_dict:
            #     count_dict[name] = 1
            # else:
            #     count_dict[name] += 1
            count_dict[name] = count_dict.get(name, 0) + 1
    
    print(count_dict)

    #{"Eliza": 1, "Xinting": 2}
    #check who has highest count
    highest_count = 0
    highest_name = ""
    for name, count in count_dict.items():
        if count > highest_count:
            highest_count = count
            highest_name = name

    print(highest_name)

    return highest_name     

    #return the name with highest count. 

visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")