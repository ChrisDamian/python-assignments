def create_ascii_banner(text):
    border = "*" * (len(text) + 4)
    return f"{border}\n* {text} *\n{border}"

# Get user input
name = input("What's your name? ")
age = input("How old are you? ")
location = input("Where are you from? ")

# Create a personalized message
message = f"Hello, {name} from {location}! You're {age} years young and amazing!"

# Print ASCII art banner
print("\n" + create_ascii_banner("Welcome!"))
print(create_ascii_banner(message))
