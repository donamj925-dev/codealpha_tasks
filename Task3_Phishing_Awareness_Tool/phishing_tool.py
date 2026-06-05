url = input("Enter website URL: ")

if url.startswith("https://"):
    print("Likely Safe Website")
else:
    print("Warning: Suspicious Website")
