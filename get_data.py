from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from time import sleep

def get_data():
    app = Application(backend = 'uia')
    app.connect(title = "AD5933 Beta Version REV1.0", found_index = 0)
    window = app.window(title = "AD5933 Beta Version REV1.0", found_index = 0)

    window.StartSweep.click_input()

    sleep(1)

    window.OK.click_input()
    window.DownloadImpedanceData.click_input()
    send_keys('{ENTER}')