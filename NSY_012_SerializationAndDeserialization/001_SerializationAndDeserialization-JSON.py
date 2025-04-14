############################################################################################################################
################################## Serialization and Deserialization #######################################################
#################################   JSON    ################################################################################
############################################################################################################################
"""
Serialization and deserialization in Python involve converting a data structure or object into a format that can be stored 
or transmitted (serialization) and then converting it back into the original structure (deserialization). The most common 
formats used for these operations are JSON and Pickle.

Here is a quick breakdown:

Serialization
Serialization is the process of converting a Python object (like a dictionary, list, or custom object) into a format such 
as JSON that can be easily saved or sent across networks.

Deserialization
Deserialization is the reverse process where the serialized data is converted back into a Python object.

Key Differences:

    JSON: Human-readable and widely used for web APIs; supports simple data types.
    Pickle: Python-specific and can serialize custom objects but isn't human-readable.

Serialization and deserialization are essential for saving data or transferring it between systems.
"""

print("################################################################################################################")
print("################################### Example-1 ###################################################################")
print("############################## Serialization via JSON ###########################################################")
print("################################################################################################################")
print("Code Output:\n")
import json

# Example dictionary
data = {"name": "Naveen", "age": 30, "city": "Bengaluru"}

# Serialization: Converting Python object to JSON
serialized_data = json.dumps(data)
print("Serialized JSON:", serialized_data)

# Deserialization: Converting JSON back to Python object
deserialized_data = json.loads(serialized_data)
print("Deserialized object:", deserialized_data)
print("################################################################################################################")

print("################################################################################################################")
print("################################### Example-2 ###################################################################")
print("############################## Serialization via JSON  (List of Dictionaries) ##################################")
print("################################################################################################################")
print("Code Output:\n")
import json

# List of dictionaries
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# Serialization
serialized_data = json.dumps(data)
print("Serialized JSON:", serialized_data)

# Deserialization
deserialized_data = json.loads(serialized_data)
print("Deserialized Object:", deserialized_data)
print("################################################################################################################")

print("################################################################################################################")
print("################################### Example-3 ###################################################################")
print("############################## Writing and Reading JSON from a File #############################################")
print("################################################################################################################")
import json

# Data to be saved
data = {"project": "AI Assistant", "status": "In Progress", "team": 5}

# Serialization: Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Deserialization: Reading JSON from a file
with open("data.json", "r") as file:
    deserialized_data = json.load(file)

print("Deserialized Object:", deserialized_data)
print("################################################################################################################")

print("################################################################################################################")
print("################################### Example-4 ###################################################################")
print("############################## Custom Objects ###################################################################")
print("################################################################################################################")
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Custom method to serialize a custom object
def person_to_json(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError("Type not serializable")

# Creating a Person object
person = Person("Naveen", 28)

# Serialization with custom logic
serialized_data = json.dumps(person, default=person_to_json)
print("Serialized JSON:", serialized_data)

# Deserialization
deserialized_data = json.loads(serialized_data)
print("Deserialized Object:", deserialized_data)
print("################################################################################################################")


