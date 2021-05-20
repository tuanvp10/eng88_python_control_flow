# Control Flow
### Control flow is very important in any programming language to control the flow of your conditions and decisions.
- if, elif and else conditions
- for and while loops

### If Statements
```
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
```
```
age = int(input("Hello!, how old are you? "))
    if age < 3:
        print("Everyone can watch.")
    elif age >= 3 and age <= 12:
        print("General viewing, but some scenes may be unsuitable for young children.")
    elif age >= 12 and age <= 14:
        print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
    elif age >=15 and age <=18:
        print("No one younger than 15 may see a 15 film in a cinema.")
    elif age >= 18:
        print("No one younger than 18 may see an 18 film in a cinema.")
  ```
### For Loops

```
# Loops are used to iterate through data
# List, dicts, sets

# First iteration
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
student_1 = {
    "name" : "Tuan",
    "key" : "value",
    "stream" : "Cyber Security", # strings
    "completed_lessons" : "3", # int
    "completed_lessons_name" : ["variables", "operators" ,"data_collections"] # list

}
for data in student_1.values():
# For values = for data in student_1.values()
    if data == "value":
        break
    print(data)
```
### While Loops

```
user_prompt = True

while user_prompt:
    age = input("How old are you?")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digits please")
    print(f"Your age is {age}")
 ```
