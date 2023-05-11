import time
import random
from colr import color # to install run "python3 -m pip install -r requirements.txt" or "pip install colr"

class Typeme:

    def __init__(self):
        input(color("Press Enter to start Typeme!!!", fore='purple', style = 'bright'))
        self.texts = open("texts.txt", "r").read().split("\n")
        self.reset()

        while self.running:
            
            countdown_time = 3
            print(f"Starting in {countdown_time} seconds...")
            for i in range (countdown_time, 0, -1):
                print(f"{i}...")
                time.sleep(1)

            print()  
            print(color(self.sample_text, fore='yellow')) #prints random sentence
            print()  
            user_input = input("Type the above text: ")


            if user_input == self.sample_text:
                self.running = False
                self.save_results()
                print(f"{color('Correct! Your typing speed: {:.2f} Words per minute'.format(self.speed), fore ='green', style = 'bright')}")
                print(f"{color(self.get_average_wpm(), fore ='blue', style = 'bright')}")
                while True:
                    # need to allow user to exit application
                    user_input = input("Press Enter to start or type 'exit' to quit...")
                    if user_input.lower() == "exit":
                        print("Exiting now...")
                        exit()
                    elif user_input == "":
                        self.reset()
                        break

            else:
                # not very DRY but need to be able to exit in both scenarios
                print(f"{color('Incorrect. Try again.', fore='red', style='bright')}")
                while True:
                    user_input = input("Press Enter to start or type 'exit' to quit...")
                    if user_input.lower() == "exit":
                        print("Exiting now...")
                        exit()
                    elif user_input == "":     
                        break


    def reset(self):
        self.sample_text = random.choice(self.texts)
        self.running = True
        self.start_time = time.time()
        self.chars_typed = 0

    def save_results(self):
        with open("results.txt", "a") as f: #"a" for append so it doesn't overwrite scores but instead adds new line to write to.
            f.write(f"Speed: {self.speed:.2f} WPM\n")

    def get_average_wpm(self):
        with open("results.txt", "r") as f:
            speeds = []
            for line in f:
                if line.startswith("Speed:"):
                    speed = float(line.split(":")[1].split("WPM")[0].strip())#extract the numbers
                    speeds.append(speed)
            if speeds:
                average_speed = sum(speeds) / len(speeds) #add all speed then divides them by the indexed lengths of all the speeds
                return f"Average speed: {average_speed:.2f} WPM"
            else:
                return "No results found."


    @property
    def speed(self):
        elapsed_time = time.time() - self.start_time - 3 #take 3 seconds off for the countdown timer
        words_typed = len(self.sample_text.split())
        wpm = (words_typed / elapsed_time) * 60
        return wpm

    def exit():
        return

    
Typeme()