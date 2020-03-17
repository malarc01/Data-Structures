# queue implementation
queue = []

# adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('z')

print('Initial Queue')
print(queue)

# Removing elements from the queue
print("\n Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise an IndexError
# as the queue is now empty

