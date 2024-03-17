class ChatGPT:
    def __init__(self):
        self.user_name = ""
        self.university = ""
        self.semester = ""

    def greet_user(self):
        print("Hi!")

    def get_user_info(self):
        self.user_name = input("What is your name? ")
        self.university = input("Which university are you from? ")
        self.semester = input("Which semester are you currently studying? ")

    def display_info(self):
        print(f"Nice to meet you, {self.user_name}!")
        print(f"You are from {self.university}.")
        print(f"You are currently studying {self.semester} semester.")


# Create an instance of the ChatGPT class
demo_chatgpt = ChatGPT()
demo_chatgpt.greet_user()
demo_chatgpt.get_user_info()
demo_chatgpt.display_info()
