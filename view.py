import tkinter
from tkinter import messagebox

CLOSING_PROTOCOL = "WM_DELETE_WINDOW"
END_OF_LINE = "\n"
KEY_RETURN = "<Return>"
TEXT_STATE_DISABLED = "disabled"
TEXT_STATE_NORMAL = "normal"
SEND = "Send"
FAIL = "I want to give up"


class CitiesGameUI(object):
    def __init__(self, client):
        self.client = client
        self.gui = None
        self.frame = None
        self.input_field = None
        self.city = None
        self.message_list = None
        self.scrollbar = None
        self.send_button = None
        self.fail_button = None

    def show(self):
        self.gui = tkinter.Tk()
        self.fill_frame()
        self.gui.protocol(CLOSING_PROTOCOL, self.on_closing)
        # return self.input_dialogs()
        return True

    def loop(self):
        self.gui.mainloop()

    def reset(self):
        self.city.set("")

    def fill_frame(self):
        self.frame = tkinter.Frame(self.gui)
        self.scrollbar = tkinter.Scrollbar(self.frame)
        self.message_list = tkinter.Text(self.frame, state=TEXT_STATE_DISABLED)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.city = tkinter.StringVar()
        self.frame.pack()
        self.input_field = tkinter.Entry(self.gui, textvariable=self.city)
        self.input_field.pack()
        self.input_field.bind(KEY_RETURN, lambda x: self.client.send())
        self.send_button = tkinter.Button(self.gui, text=SEND, command=self.client.send)
        self.send_button.pack()
        self.fail_button = tkinter.Button(self.gui, text=FAIL, command=self.client.send_fail)
        self.fail_button.pack()

    def alert(self, title, message):
        messagebox.showerror(title, message)

    def show_message(self, message):
        self.message_list.configure(state=TEXT_STATE_NORMAL)
        self.message_list.insert(tkinter.END, str(message) + END_OF_LINE)
        self.message_list.configure(state=TEXT_STATE_DISABLED)

    def on_closing(self):
        self.client.exit()
        self.gui.destroy()