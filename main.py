from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from GUI import BombPartyGUI
import random


def get_bot_delay(difficulty_lvl: int):
    """
    A function that get a lvl of difficulty (int from 0 to 3 included)
    as input and return an delay in ms that the bot will have to
    wait before giving is answer"""

    if difficulty_lvl == 0:
        delay = random.uniform(3, 8)
        return delay

    elif difficulty_lvl == 1:
        delay = random.uniform(1, 4)
        return delay

    elif difficulty_lvl == 2:
        delay = random.uniform(0.2, 2)
        return delay
    else:
        return 0


def main():
    game_gui = BombPartyGUI()
    game_gui.mainloop()

    with open(f'{game_gui.language}_dict.txt', 'r', encoding='UTF-8') as file:
        my_dict = [i.strip() for i in file]

    # Setup Driver
    s = Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True

    # Initialize Driver
    driver = webdriver.Chrome(service=s, options=options)

    driver.get(game_gui.room_link)
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
        # Check if a game is currently on
        round_ = driver.find_element(By.CLASS_NAME, 'round')
        if round_.is_displayed():

            while True:  # Run until the game is over
                self_turn = driver.find_element(By.CLASS_NAME, 'selfTurn')


                # Check if it is bot's turn to play
                if self_turn.is_displayed():

                    # Check the current syllable
                    syllabe = driver.find_element(By.CLASS_NAME, "syllable").text.lower()

                    # Look in the dict for a word with the given syllable
                    for word in my_dict:
                        if syllabe in word:
                            time.sleep(get_bot_delay(game_gui.difficulty))
                            # Type and send the word
                            answer_input = driver.find_element(By.CSS_SELECTOR, '.selfTurn input')
                            answer_input.send_keys(word)
                            answer_input.send_keys(Keys.ENTER)
                            # Remove the word from the dict
                            my_dict.remove(word)
                            time.sleep(0.2)
                            break
                    pass

                round_ = driver.find_element(By.CLASS_NAME, 'round')  # this element is visible
                if round_.is_displayed():
                    pass
                else:
                    print("La partie est finie")
                    time.sleep(5)
                    join_button = driver.find_element(By.CSS_SELECTOR, '.join button')
                    join_button.send_keys(Keys.ENTER)
                    break



        else:
            # print("Element not found")
            time.sleep(0.5)


if __name__ == '__main__':
    main()
