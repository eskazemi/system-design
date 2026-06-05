# Python program to demonstrate working of HashTable 

# Initialize the hash table with 10 empty lists (each index is a list to handle collisions)
hashTable = [[] for _ in range(10)]

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n // 2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    # Check if the key already exists in the list to update it, otherwise append
    found = False
    for i, kv in enumerate(hashTable[index]):
        if kv[0] == key:
            hashTable[index][i] = (key, data)  # Update existing key-value pair
            found = True
            break
    if not found:
        hashTable[index].append((key, data))  # Add new key-value pair if not found


def removeData(key):
    index = hashFunction(key)
    # Remove the key-value pair from the list if it exists
    for i, kv in enumerate(hashTable[index]):
        if kv[0] == key:
            del hashTable[index][i]
            break


# Test the hash table
insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")
insertData(213, "orange")  # This should update the value for key 213

print(hashTable)

removeData(123)

print(hashTable)