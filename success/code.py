from datetime import datetime


def record_success(success_message):
    with open("success_records.txt", "a") as file:
        file.write(success_message + "\n\n")

    print("Success recorded!")

# Example usage:
success_message = "Task completed successfully on {}".format(datetime.now())
record_success(success_message)
    
