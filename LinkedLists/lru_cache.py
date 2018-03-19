# Least recently used Cache
# APIs Get(key), Set(key), Delete(key)
# private: evict() - deletes the item with oldest timestamp
# Use hashmap of key to reference. Reference is pointing to a node in doubly linked list containing key (and prev/next pointers).
# Timestamp is not needed now, as doubly linked list maintains order of elements.
# For set, create node and add it to tail of doubly linked list. If node is present or get is called,
# move it to tail of list. This needs prev and next that's why doubly linked list.
# For evict, delete the tail and its entry from hash map.
