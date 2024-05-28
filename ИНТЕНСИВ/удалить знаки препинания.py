string = input()
symbols_to_remove = ".,;:-?!"
for symbol in symbols_to_remove:
    string = string.replace(symbol, "")

print(string)

# Убирает знаки в одном слове
string = input().strip(".,;:-?!")
print(string)