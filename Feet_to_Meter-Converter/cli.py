import functions

feet_inches = input("enter feet and inches: ")


parsed = functions.parse(feet_inches)

result = functions.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is small.")
else:
    print("Kid can use the slide.")



