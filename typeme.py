import time
import random


class Typeme:

    def __init__(self):
        input("Press Enter to start the typing speed test...")
        self.texts = open("texts.txt", "r").read().split("\n")
        self.reset()

        while self.running:
            print()  # Add a line break
            print(self.color_text(self.sample_text, "yellow"))
            print()  # Add a line break
            user_input = input("Type the above text: ")

            if user_input == self.sample_text:
                self.running = False
                self.save_results()
                print(f"{self.color_text('Correct! Your typing speed: {:.2f} Words per minute'.format(self.speed), 'green')}")
                print(f"{self.color_text(self.get_average_wpm(), 'blue')}")
                input("Press Enter to start the typing speed test...")
                self.texts = open("texts.txt", "r").read().split("\n")
                self.reset()

            else:
                print(f"{self.color_text('Incorrect. Try again.', 'red')}")
                input("Press Enter to start the typing speed test...")
                self.reset()


    def reset(self):
        self.sample_text = random.choice(self.texts)
        self.running = True
        self.start_time = time.time()
        self.chars_typed = 0

    def save_results(self):
        with open("results.txt", "a") as f:
            f.write(f"Speed: {self.speed:.2f} WPM\n")

    def get_average_wpm(self):
        with open("results.txt", "r") as f:
            speeds = []
            for line in f:
                if line.startswith("Speed:"):
                    speed = float(line.split(":")[1].split("WPM")[0].strip())
                    speeds.append(speed)
            if speeds:
                average_speed = sum(speeds) / len(speeds)
                return f"Average speed: {average_speed:.2f} WPM"
            else:
                return "No results found."


    @property
    def speed(self):
        elapsed_time = time.time() - self.start_time
        words_typed = len(self.sample_text.split())
        wpm = (words_typed / elapsed_time) * 60
        return wpm

    def color_text(self, text, color='white'):
        colors = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
        }
        end_color = '\033[0m'
        return f"{colors[color]}{text}{end_color}"

    
Typeme()