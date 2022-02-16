# importing the module
import wikipedia

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

for it in results:
    print(it + "\n")
    print(results[it])
    print("\n\n")
# result_sum = wikipedia.summary(result[0][0])

# print("Summary Argument suggested:\n")
# print(result_sum)