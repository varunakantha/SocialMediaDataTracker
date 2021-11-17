# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import executors

target_page = "https://www.facebook.com/photo/?fbid=481582996655712&set=a.410077400472939"
target_element = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/span/div/span[2]/span/span"

if __name__ == '__main__':
    executor = executors.MainExecutor()

    if executor.login("email", "password"):

        executor.start_data_stream(target_page,target_element)

    else:
        print("Ooops! Unable to login to account.")









