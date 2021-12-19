import pyautogui
import random
import time

interrupt_messages = [
    'Remember, hit Control+C to exit when you're done.',
    'Done jumping around your FC estate? Control+C.',
    'Maybe go outside for a bit. Hit Control+C to quit this charade.',
    'If such a lengthy idle session was not your intention, hit Control+C.'
    ]
exit_messages = [
    'Okay, bye!', 
    'Thanks for doing your part to make queues longer <3', 
    'You no longer know La Hee.',
    'Yeah, well, whatever, quit if you want, quitter.']

def press_space():
    jump_counter = 0
    while True:
        try:
            pyautogui.press('space')
            sleeptime = random.randint(10,60)
            print(f"Sleeping for {sleeptime} seconds, then hoppin' again.")
            jump_counter += 1
            if jump_counter % 5 == 0:
                print(random.choice(interrupt_messages))
            time.sleep(sleeptime)
        except KeyboardInterrupt:
            print(random.choice(exit_messages))
            if jump_counter == 1:
                print("You jumped one time! That's not very much.")
            else:
                print(f"You jumped {jump_counter} times this session!")
            break

if __name__ == "__main__":
    print("Waiting 5 seconds before proceeding. Alt-tab already!")
    time.sleep(5)
    press_space()