# # Control flow with if, elif and else - loops
#
# weather = "sunny"
#
# if weather == "sunny": # If this condition is 'True' execute the next line of code
#     print("Enjoy the weather! ") # If 'True' this line will be executed
# if weather != "sunny":
#     print("Wait for it to be sunny again!")
# if weather == "cloudy":
#     print("Let us hope it does not rain!")
# elif weather == "raining":
#     print("Take a umbrella!")
# else:
#     print("Oops sorry something went wrong, please try again! ") # If 'False' this line will be executed
# # Add a condition to use elif when the condition is 'False'

# Loops
# Loops are used to iterate through data
# List, dicts, sets

#First iteration
list_data = [1, 2, 3, 4, 5]
print(list_data)

for list in list_data:
    if list == 3:
        print("I found 3")
    if list == 2:
        print("I found 2")
    if list == 5:
        print("This is the last number and I found it aswell")
else:
    print("Better luck next time!")



# Second iteration
# student_1 = {
#     "name" : "Tuan",
#     "key" : "value",
#     "stream" : "Cyber Security", # strings
#     "completed_lessons" : "3", # int
#     "completed_lessons_name" : ["variables", "operators" ,"data_collections"] # list
#
# }
# for data in student_1.values():
# # For values = for data in student_1.values()
#     if data == "value":
#         break
#     print(data)

