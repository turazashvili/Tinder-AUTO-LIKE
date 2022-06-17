from time import sleep
import webbrowser 
import pyautogui
import threading
import keyboard

# Opens Tinder website in browser
url = 'https://tinder.com/'
webbrowser.open(url)

# Sleep time for making sure Tinder has loaded before loop starts. Don't suggest decreasing the sleep time.
sleep(10) 

def like():
    while True:
        
        try:
            # searches for Like button based on like.png file. You can change the like.png file if like button looks different for you.
            cords = pyautogui.locateCenterOnScreen('like.png', confidence=0.9)
            pyautogui.moveTo(cords)
            pyautogui.click(cords)
        except:
            print("Try again")

        # Stops the script with long press of 'S' button on your keyboard.
        if keyboard.is_pressed('S'):
            print("\nYou finished Tindering")
            break
    

threading.Thread(target=like, daemon=True).start()
input('Press Enter to exit.')
