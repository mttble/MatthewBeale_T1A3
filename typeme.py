import time
import random


class Typeme:

    def __init__(self):
        input("Press Enter to start Typeme!!!")
        self.texts = open("texts.txt", "r").read().split("\n")
        self.reset()

        while self.running:
            
            countdown_time = 3
            print(f"Starting in {countdown_time} seconds...")
            for i in range (countdown_time, 0, -1):
                print(f"{i}...")
                time.sleep(1)

            print()  
            print(self.color_text(self.sample_text, "yellow")) #prints random sentence
            print()  
            user_input = input("Type the above text: ")


            if user_input == self.sample_text:
                self.running = False
                self.save_results()
                print(f"{self.color_text('Correct! Your typing speed: {:.2f} Words per minute'.format(self.speed), 'green')}")
                print(f"{self.color_text(self.get_average_wpm(), 'blue')}")
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
                print(f"{self.color_text('Incorrect. Try again.', 'red')}")
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

    def color_text(self, text, color='white'):
        colors = {
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
        }
        end_color = '\033[0m'
        return f"{colors[color]}{text}{end_color}"
    
    def exit():
        return

    
Typeme()