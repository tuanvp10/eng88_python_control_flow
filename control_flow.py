# Control flow with if, elif and else - loops

weather = "sunny"

if weather == "sunny": # If this condition is 'True' execute the next line of code
    print("Enjoy the weather! ") # If 'True' this line will be executed
if weather != "sunny":
    print("Wait for it to be sunny again!")
if weather == "cloudy":
    print("Let us hope it does not rain!")
elif weather == "raining":
    print("Take a umbrella!")
else:
    print("Oops sorry something went wrong, please try again! ") # If 'False' this line will be executed
# Add a condition to use elif when the condition is 'False'


