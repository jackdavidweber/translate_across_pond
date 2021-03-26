import json

def americanize(string):
    with open('british_to_american.json') as json_file:
        british_to_american = json.load(json_file)

    for british_spelling, american_spelling in british_to_american.items():
        string = string.replace(british_spelling, american_spelling)
    
    return string

def britishize(string):
    with open('american_to_british.json') as json_file:
        american_to_british = json.load(json_file)

    for american_spelling, british_spelling in american_to_british.items():
        string = string.replace(american_spelling, british_spelling)
    
    return string