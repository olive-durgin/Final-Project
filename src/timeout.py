import threading

def get_input():
    user_input = input("Enter something: ")
    print(f"You entered: {user_input}")

# Create a thread for the input function
input_thread = threading.Thread(target=get_input)
input_thread.start()

# Wait for the thread to complete or timeout
input_thread.join(timeout=5)

if input_thread.is_alive():
    print("No input received within the timeout period.")
    # Optionally, you can stop the thread if needed
