"""
Project 7 - Hash Tables
CSE331 - F19
Project Created By: Wendy Fogland
Project Completed By: Heather Noonan
"""


class HashNode:
    """
	DO NOT EDIT
	"""

    def __init__(self, key, value, available=False):
        self.key = key
        self.value = value
        self.is_available = available

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
	Hash Table Class
	"""

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=7):
        """
		DO NOT EDIT
		Initializes hash table
		:param capacity: how much the hash table can hold
		"""

        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        for prime in self.primes:
            if self.capacity <= prime:
                self.prime = prime
                break

    def __eq__(self, other):
        """
		DO NOT EDIT
		Equality operator
		:param other: other hash table we are comparing with this one
		:return: bool if equal or not
		"""

        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
		DO NOT EDIT
		Represents the table as a string
		:return: string representation of the hash table
		"""

        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _is_available(self, j):
        """
		DO NOT EDIT
		Check if the index in the table is available/empty
		:param j: index in the table
		:return: True if available or empty, false otherwise
		"""
        return self.table[j] is None or self.table[j].is_available is True

    def hash_first(self, key):
        """
		DO NOT EDIT
		Converts key, a string, into a bin number for the hash table
		:param key: key to be hashed
		:return: bin number to insert hash item at in our table, -1 if val is an empty string
		"""

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def hash_second(self, key):
        """
		Hashes key based on prime number for double hashing
		DO NOT EDIT
		:param key: key to be hashed
		:return: a hashed value
		"""

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        hashed_value = self.prime - (hashed_value % self.prime)
        if hashed_value % 2 == 0:
            hashed_value += 1

        return hashed_value

    def get_load_factor(self):
        """
        Gets the load factor of the table (size/capacity)
        :return: the load factor
        """
        return self.size / self.capacity

    def double_hashing(self, key, inserting=False):
        """
        Returns an index at which the key parameter can be inserted into the table
        :param key: the key of the hash node
        :param inserting: True if inserting the key, False otherwise (for delete/searching)
        :return: the index of where the key can be inserted
        """
        i = 0
        index = (self.hash_first(key) + i * self.hash_second(key)) % self.capacity
        if inserting:
            while not self._is_available(index):
                if self.table[index].key == key:
                    return index
                i += 1
                index = (self.hash_first(key) + i * self.hash_second(key)) % self.capacity
            return index
        else:
            while self.table[index] is not None:
                if self.table[index].key == key:
                    return index
                i += 1
                index = (self.hash_first(key) + i * self.hash_second(key)) % self.capacity
            return index

    def insert(self, key, value):
        """
        Inserts a key, value pair into the hash table
        :param key: the key of the key, value pair, determines where to insert the node
        :param value: the value of the hash node
        :return: none
        """
        index = self.double_hashing(key, True)
        if self.table[index] is None or self.table[index].is_available:
            self.size += 1
        self.table[index] = HashNode(key, value)

        if self.get_load_factor() >= 0.4:
            self.grow()

    def search(self, key):
        """
        Searches for a given key in a hash table
        :param key: the key to be searched for
        :return: returns the node with the given key if found, or none otherwise
        """
        index = self.double_hashing(key)
        if self.table[index] is not None and self.table[index].key == key:
            return self.table[index]
        else:
            return None

    def grow(self):
        """
        Doubles the capacity of the hash table
        :return: none
        """
        for prime in self.primes:
            if (self.capacity*2) <= prime:
                self.prime = prime
                break
        self.rehash()

    def rehash(self):
        """
        When the has table needs to grow, this function puts all the nodes
        currently in the hash table into a list, doubles the capacity and clears
        the hash table, then inserts the old nodes into the newly sized list
        size
        :return: none
        """
        nodes = []
        for node in self.table:
            if node is not None and node.is_available is False:
                nodes.append(node)
        self.capacity = self.capacity * 2
        self.size = 0
        self.table = [None] * self.capacity
        for item in nodes:
            self.insert(item.key, item.value)

    def delete(self, key):
        """
        Deletes the node with the given key, if it exists
        :param key: the key to delete
        :return: none
        """
        if key is not None:
            node = self.search(key)
            if node is not None and node.is_available is False:
                node.key = None
                node.value = None
                node.is_available = True
                self.size -= 1


def anagrams(string1, string2):
    """
    Determines if two strings are anagrams
    :param string1: the first string
    :param string2: the second string
    :return: a boolean value representing whether the two strings are anagrams
    """
    if string1 is None or string2 is None:
        return False
    string2 = string2.replace(" ", "")
    string1 = string1.replace(" ", "")
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        return False
    hsh = HashTable()
    for char in string1:
        hsh.insert(char, 0)

    for char in string2:
        hsh.delete(char)
    if hsh.size == 0:
        return True
    else:
        return False


