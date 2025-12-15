text = "  Python Programming  "

print("Original text:", text)
print("Lowercase the text:", text.lower())
print("Uppercase the text:", text.upper())
print("Strip:", text.strip())
print("Replacing the word:", text.replace("Python", "Java"))
print("Find the word index:", text.find("Program"))
print("Count of  letter 'm':", text.count("m"))
print("Starts with Python:", text.strip().startswith("Python"))
print("Ends with ing:", text.strip().endswith("ing")) 
print("Lowercase+Uppercase",text.swapcase())
print("Adding symbols in between","-".join(["Python","Programming"]) )