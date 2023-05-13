import time
import random
from colr import color  # to install run "python3 -m pip install -r requirements.txt" or "pip install colr"

# PEP 8 styling guide 

class Typeme:

    def __init__ (self):
        input(color("Press Enter to start Typeme!!!", fore = 'purple', style = 'bright'))
        
        self.start()


        while self.running:

            if not self.select_difficulty:  # added check to see if difficulty has been selected
                self.select_difficulty()
                self.difficulty_selected = True
            
            # Countdown timer
            countdown_time = 3
            print(f"Starting in {countdown_time} seconds...")
            for i in range (countdown_time, 0, -1):
                print(f"{i}...")
                time.sleep(1)
            
            print()
            print(color(self.sample_text, fore='yellow'))  # prints random sentence
            print()
            
            user_input = input("Type the above text: ")


            if user_input == self.sample_text.strip():
                self.running = False  # stops while loop
                self.save_results()  # calls save results function
                print(color(f"Correct! Your typing speed: {self.speed:.2f} Words per minute", fore = 'green', style = 'bright'))
                print(f"{color(self.get_average_wpm(), fore = 'blue', style = 'bright')}")
                while True:
                            self.start()
                            break

            else:
                print(f"{color('Incorrect. Try again.', fore = 'red', style = 'bright')}")
                self.start()
    
    def select_difficulty(self):
        while True: 
            while self.difficulty not in ["e", "m", "h", "exit"]:
                self.difficulty = input(color("Select difficulty level type 'e','m' or 'h' for easy, medium, hard or 'exit' to quit: ", fore = 'pink')).lower()
            if self.difficulty == "e":
                self.difficulty = "easy"
            elif self.difficulty == "m":
                self.difficulty = "medium"
            elif self.difficulty == "h":
                self.difficulty = "hard"
            else:
                print("Exiting now...")
                exit()
            return True

    def load_texts(self):
        try:
            with open(f"texts{self.difficulty}.txt", "r") as f:
                self.texts = f.readlines()
        except FileNotFoundError:
            print(f"Error: texts{self.difficulty}.txt not found.")

    

    def start(self):
        self.difficulty = ""
        self.select_difficulty()
        self.load_texts()
        self.sample_text = random.choice(self.texts)
        self.running = True
        self.start_time = time.time()
        

    def save_results(self):
        with open("results.txt", "a") as f:  # "a" for append so it doesn't overwrite scores but instead adds new line to write to.
            f.write(f"Difficulty: {self.difficulty.capitalize()} | Speed: {self.speed:.2f} WPM\n")

    def get_average_wpm(self):
        with open("results.txt", "r") as f:
            speeds = []
            for line in f:
                if line.startswith("Difficulty:"):
                    speed = float(line.split("| Speed:")[1].split("WPM")[0].strip())  # extract the numbers
                    speeds.append(speed)
            if speeds:
                average_speed = sum(speeds) / len(speeds)  # add all speed then divides them by the indexed lengths of all the speeds
                return f"Average speed: {average_speed:.2f} WPM"
            else:
                return "No results found."


    @property  # getter method for the speed attribute
    def speed(self):
        elapsed_time = time.time() - self.start_time - 3  # take 3 seconds off for the countdown timer
        words_typed = len(self.sample_text.split())
        wpm = (words_typed / elapsed_time) * 60
        return wpm  # returns calculated wpm to 

    
Typeme()
