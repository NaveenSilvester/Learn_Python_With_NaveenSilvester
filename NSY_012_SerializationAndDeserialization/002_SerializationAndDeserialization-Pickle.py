############################################################################################################################
################################## Serialization and Deserialization #######################################################
#################################   Pickle    ################################################################################
############################################################################################################################

print("\n################################################################################################################")
print("################################### Example-1 ###################################################################")
print("############################## Serialization via Pickle ##########################################################")
print("################################################################################################################")
print("Code Output:\n")
import pickle

# Example dictionary
data = {"name": "Naveen", "age": 30, "city": "Bengaluru"}

# Serialization: Converting Python object to byte stream
serialized_data = pickle.dumps(data)
print("Serialized Pickle:", serialized_data)

# Deserialization: Converting byte stream back to Python object
deserialized_data = pickle.loads(serialized_data)
print("Deserialized object:", deserialized_data)
print("################################################################################################################\n")

print("\n################################################################################################################")
print("################################### Example-2 ###################################################################")
print("############################## Serialization via Pickle ##########################################################")
print("################################################################################################################")
print("Code Output:\n")
import pickle

# Python object
data = {"project": "AI Assistant", "status": "In Progress", "team": 5}

# Serialization: Write object to file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Deserialization: Read object back from file
with open("data.pkl", "rb") as file:
    deserialized_data = pickle.load(file)

print("Deserialized Object:", deserialized_data)
print("################################################################################################################\n")

print("################################################################################################################")
print("################################### Example-3 ###################################################################")
print("############################## Custom Objects ###################################################################")
print("################################################################################################################")
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Create a Person object
person = Person("Naveen", 28)

# Serialization: Convert custom object to binary
serialized_person = pickle.dumps(person)
print("Serialized Person:", serialized_person)

# Deserialization: Convert binary back to custom object
deserialized_person = pickle.loads(serialized_person)
print("Deserialized Person:", deserialized_person)
print("################################################################################################################\n")