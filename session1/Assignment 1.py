print("Hello there! Im a simple chatbot that wants to get to know you better.")

name = input("What's your name? ").strip()
age = input("How old are you? ").strip()
food = input("What's your favorite food? ").strip()

print() # Biar keliatan rapi, kasih jarak satu baris
# Rangkuman
print(f"Nice to meet you {name}!")
print(f"You are {age} years old and like {food}. What a coincidence! I also like {food}!")
