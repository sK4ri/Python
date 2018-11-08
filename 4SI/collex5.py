dict = {"Jane Doe": "+27 555 5367", "John Smith": "+27 555 6254", "Bob Stone": "+27 555 5689"}
print(dict)
dict["Jane Doe"] = "+27 555 1024"
print(dict)
dict.update({"Anna Cooper": "+27 555 3237"})
print(dict)
print(dict.get("Bob Stone"))
print(dict.keys())
print(dict.values())
print(dict.items())
