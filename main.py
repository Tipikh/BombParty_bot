from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pyinputplus import inputStr
import time
import re
from GUI import BombPartyGUI

global link_room
global bot_name
def main():
    game_gui = BombPartyGUI()

    game_gui.mainloop()

    with open('fr_dict.txt', 'r', encoding='UTF-8') as file:
        my_dict = [i.strip() for i in file]

    # Setup Driver
    s = Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True

    # Initialize Driver
    driver = webdriver.Chrome(service=s, options=options)

    driver.get(game_gui.link_room)
    driver.implicitly_wait(5)

    time.sleep(1)

    # Log In
    nickname = driver.find_element(By.CSS_SELECTOR, ".setNickname input")
    nickname.send_keys(game_gui.bot_name)
    nickname.send_keys(Keys.ENTER)

    # Join room
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    join_button = driver.find_element(By.CSS_SELECTOR, '.join button')
    join_button.send_keys(Keys.ENTER)

    while True:
        round_ = driver.find_element(By.CLASS_NAME, 'round')
        if round_.is_displayed():

            while 1:  # Run until the game is over

                self_turn = driver.find_element(By.CLASS_NAME, 'selfTurn')
                player_turn = driver.find_element(By.CLASS_NAME, "player")

                # Check if it is bot's turn to play
                if self_turn.is_displayed():

                    # Check the current syllable
                    syllabe = driver.find_element(By.CLASS_NAME, "syllable").text.lower()

                    # Look in the dict for a word with the given syllable
                    for word in my_dict:
                        if syllabe in word:
                            # Type and send the word
                            answer_input = driver.find_element(By.CSS_SELECTOR, '.selfTurn input')
                            answer_input.send_keys(word)
                            answer_input.send_keys(Keys.ENTER)
                            # Remove the word from the dict
                            my_dict.remove(word)
                            time.sleep(0.5)
                            break
                    pass

                round_ = driver.find_element(By.CLASS_NAME, 'round')  # this element is visible
                if round_.is_displayed():
                    pass
                else:
                    break


        else:
            # print("Element not found")
            time.sleep(0.5)


if __name__ == '__main__':
    main()
