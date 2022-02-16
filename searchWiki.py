import wikipedia

def search(argument):
    #set lang
    wikipedia.set_lang("it")

    # finding result for the search
    # sentences = 2 refers to numbers of line
    result = wikipedia.search('astronomia', results = 5, suggestion = True)

    # printing the result
    print("Arguments:\n")
    results ={}
    for arg in result[0]:
        # print(wikipedia.summary(arg))
        # print("\n\n")
        results[arg] = wikipedia.summary(arg)
        
    return results