import queue
import time
import random

class Request:
    def __init__(self, request_id):
        self.request_id = request_id

    def __str__(self):
        return f"Request ID: {self.request_id}"

def generate_request(q, request_counter):
    """ Generate a new request and add it to the queue """
    request = Request(request_counter)
    q.put(request)
    print(f"Generated {request}")

def process_request(q):
    """ Process the next request in the queue """
    if not q.empty():
        request = q.get()
        print(f"Processing {request}")
    else:
        print("Queue is empty.")

def main():
    q = queue.Queue()
    request_counter = 1  # Initial request ID

    # Simulation loop
    while True:
        generate_request(q, request_counter)
        process_request(q)
        request_counter += 1
        time.sleep(random.uniform(0.1, 0.3))  # Pause for realism



from collections import deque

def is_palindrome(s):
    """ Check if the given string is a palindrome, ignoring spaces and case sensitivity. """
    # Clean the string: remove spaces and convert to lower case
    cleaned_string = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Use deque for efficient pop from both ends
    char_deque = deque(cleaned_string)
    
    # Check characters from both ends
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

