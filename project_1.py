class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    
class DLL: #Doubly Linked List
    def __init__(self, head=None,tail=None):
        self.head = head
        self.tail = tail
        
    def remove(self, node):
        if self.head is None:
            return
        
        if node.prev:
            node.prev.next = node.next
        else :
            self.head = node.next
 
        if node.next :
            node.next.prev = node.prev
        else :
            self.tail = node. prev
    
    
    def add_tail(self, node):
        if self.head == None and self.tail == None:
            self.tail = self.head = node
            return
     
        self.tail.next = node
        node.next = None
        node.prev = self.tail
        self.tail = node
     
        
            

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = DLL()
        self.size = 0
        self.existing_keys = {} #The dictionary contains all the existing_entries

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. \
        if key not in self.existing_keys:
            return -1
        return_node = self.existing_keys[key]
        self.cache.remove(return_node)
        return return_node.value
            
        

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.existing_keys:
            self.existing_keys[key].value = value
        else: 
            new_node = Node(key, value)
            self.existing_keys[key] = new_node
            self.cache.add_tail(new_node)
            #print(self.cache.head.value)
            self.size += 1
            if self.size > self.capacity:
                del self.existing_keys[self.cache.head.key]
                self.cache.remove(self.cache.head)
                self.size -= 1
                


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
# Your work here