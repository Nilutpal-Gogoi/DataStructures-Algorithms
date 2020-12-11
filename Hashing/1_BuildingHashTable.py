# Here we'll use chaining strategy along with the resize operation to avoid collisions in the table.
# All the elements with the same hash key will be stored in a linked list at that index. In data structures, these lists
# are called buckets. The size of the hash table is set as n*m where n is the number of keys it can hold and m is the
# number of slots each bucket contains.

# Implementation -
# We will start by building a simple HashEntry class. As discussed earlier, a typical hash entry consists of three data
# members: the key, the value, and the reference to a new entry.


class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None


# Now, we'll create the HastTable class which is a collection of HashEntry objects. We will also keep track of the total
# number of slots in the hash table and the current size of the hash table.


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots

    # Helper functions

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash function - It maps values to a slot in the hash table.
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    # RESIZING IN A HASH TABLE
    # We'll make sure that the hash table doesn't get loaded up beyond a certain threshold. Whenever it crosses the
    # threshold, we shift the elements from the current table to a new table with double the capacity. This helps us to
    # avoid collisions.
    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for i in range(0, len(self.bucket)):
            head = self.bucket[i]
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.nxt
                head = head.nxt
        self.bucket = new_bucket
        self.slots = new_slots

    # INSERTION IN TABLE
    # Insertion in hash tables is a simple task and it usually takes a constant amount of time. When the hash function
    # returns the index for our input key, we check if there is a hash entry already present at that index (if it does,
    # a collision has occurred). if not, we simply create a new hash entry for the key/value. However, if the index is
    # not None, we will traverse through the bucket to check if an object with our key exists.

    def insertion(self, key, value):
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            print(key, "-", value, "inserted at index:", b_index)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head:
                if head.key == key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    print(key, "-", value, "inserted at index:", b_index)
                    self.size += 1
                    break
                head = head.nxt
        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    # SEARCHING IN HAST TABLE
    # Search takes O(1) amount of time. The search function takes in a key and sends it through the hash function to get
    # the corresponding index in the table. If the hash entry with the desired key/value pair is found at that index,
    # its value is returned.

    def search(self, key):
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # Search key in the slots
        while head:
            if head.key == key:
                return head.value
            head = head.nxt
        # If key not found
        return None

    # DELETION IN TABLE
    # Deletion can take up to O(n) time where n is the no of hash entries in the table.
    # If they all get stored in the same bucket, we would have to traverse teh whole bucket to reach the entry we want
    # to delete. The average case is still O(1)

    # Remove a value based on a key
    def delete(self, key):
        # Find index
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # If key exists at first slot
        if head.key == key:
            self.bucket[b_index] = head.nxt
            print(key, "-", head.value, "deleted")
            # Decrease the size by one
            self.size -= 1
