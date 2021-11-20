# 1. Implement a hash for text. Given a string as input, construct a hash with words as keys, and word counts as values.
#    Your implementation should include:
#      a) Linked List to handle collision
#      b) operations: insert(key), delete(key), find(key), increase(key), list-all-keys
# Each word or key can only appear once in the datastructure
#

import re
import random
import math

# Create Node


class Node():
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

# Create LinkedList Structure


class LinkedList():
    def __init__(self):
        self.head = None

    # Finds the key within a LinkedList
    def find_index_LL(self, key):
        index = 0
        itr = self.head
        while itr is not None:
            if(itr.key == key):
                return index
            itr = itr.next
            index += 1
        return -1

    # Inserts the key within a LinkedList if it appears for the first time
    def insert_LL(self, key, value):
        # The first node in a linkedlist
        if self.head is None:
            self.head = Node(key, value)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        # Attach every subsequent node to the LL
        itr.next = Node(key, value)

    # Increase the count if key is already present else call insert_LL
    def increase_LL(self, key):
        if self.find_index_LL(key) != -1:
            i = self.find_index_LL(key)
            node = self.head
            while(i > 0):
                node = node.next
                i -= 1
            node.value += 1
            return
        else:
            self.insert_LL(key, 1)

    # Print the Linked List
    def print_ll(self):
        #LL is empty
        if self.head is None:
            llstr = '-'
            return llstr
        #LL is not empty
        itr = self.head
        llstr = ''
        while itr:
            llstr += '('+str(itr.key)+','+str(itr.value)+')' + ' --> '
            itr = itr.next
        return llstr

    # Delete the key if its count is 1 else decrease the count
    def delete_ll(self, key):
        if self.find_index_LL(key) != -1:
            count = self.find_index_LL(key)

            # Key is at the head
            if(count == 0):
                if(self.head.value > 1):
                    self.head.value -= 1
                    return
                else:
                    cur = self.head
                    self.head = self.head.next
                    cur.next = None
                    return

            # Key not at head
            prev = self.head
            while(count > 1):
                prev = prev.next
                count -= 1
            cur = prev.next
            if(cur.value > 1):
                cur.value -= 1
                return
            else:
                prev.next = cur.next
                cur.next = None
                return
        else:
            print('Delete failed: Key not Found!!!')
            return

# Define Universal Hash Function


def Hash(key):
    random.seed(1)
    # Large prime number
    p = 23330488122150822469
    a = random.randrange(p)
    b = random.randrange(p)
    num = 0
    for i in key:
        num += ord(i)
    return ((a*num+b) % p) % size

# Invoke increase_LL on a linkedlist present at Hash index corresponding to a key


def increase(key):
    h = Hash(key)
    # Search for the key within the List
    HashTable[h].increase_LL(key)

# Invove delete_ll on a linkedlist present at Hash index corresponding to a key


def delete(key):
    h = Hash(key)
    HashTable[h].delete_ll(key)

# Find the index of the key


def find(key):
    h = Hash(key)
    if HashTable[h].find_index_LL(key) != -1:
        print('Found the key at the HashTable Index '+str(h))
    else:
        print('Key not found!!!')

# Print all the keys within the hashtable


def list_all_keys():
    for i in range(size):
        line = str(HashTable[i].print_ll())
        print(str(i)+": "+line)


if __name__ == '__main__':
    my_file = open('..\\Input_Files\\poem.txt', 'r')
    my_content = my_file.read()
    word_list = re.findall('([a-zA-Z]+)', my_content)
    size = math.ceil(len(word_list)/10)
    # List comprehension to declare an array of nodes
    HashTable = [LinkedList() for i in range(size)]

    for item in word_list:
        increase(item)

    list_all_keys()
    # delete('Perhaps')
    # delete('shedding')
    # delete('hatching')
    # delete('branches')
    # # delete('specific')
    # # delete('disclaim')
    # delete('Lewis')
    # delete('Lewis')
    # # delete('employees')
    # list_all_keys()
    # find('agree')
    # find('Pramodh')
