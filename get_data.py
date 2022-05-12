from pywinauto.application import Application

app = Application()
app.connect(title = "AD5933 Beta Version REV1.0", found_index = 0)

window = app.window(title = "AD5933 Beta Version REV1.0", found_index = 0)
window.close()

