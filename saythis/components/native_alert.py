from kivy.utils import platform

platform = platform()


class AlertPrint():
    ''' Prints the alert to the console
    '''
    
    def __init__(self, message):
        self.message = message
    
    def show_alert(self):
        print("ALERT: {}".format(self.message))


class AlertTkinter():
    ''' Shows the alert using a pop-up Tkinter window
    '''
    
    def __init__(self, message):
        self.message = message
        
    def _center_window(self, app):
        w = app.winfo_screenwidth()
        h = app.winfo_screenheight()
        rootsize = tuple(int(_) for _ in app.geometry().split('+')[0].split('x'))
        x = w/2 - rootsize[0]/2
        y = h/2 - rootsize[1]/2
        return "%dx%d+%d+%d" % (rootsize + (x, y))
    
    def show_alert(self):
        import Tkinter
        master = Tkinter.Tk()
        label = Tkinter.Label(text=self.message).pack(expand=True)
        frame = Tkinter.Frame(master, 
                              width=320, height=160, 
                              bg="", colormap="new")
        frame.pack(fill=Tkinter.X, padx=5, pady=5)
        frame.after(5000, master.destroy)
        
        master.update_idletasks()
        master.geometry(self._center_window(master))
        master.mainloop()


class AlertToast():
    ''' Shows the alert using the native Android Toast feature
    '''
    
    def __init__(self, message):
        self.message = message
        
    def show_alert(self):
        from jnius import autoclass
        from jnius import cast
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        Toast = autoclass('android.widget.Toast')
        toast = Toast(PythonActivity.mActivity)
        #toast.setDuration(Toast.LENGTH_SHORT)
        #EditableFactory = autoclass('android.text.Editable.Factory')
        #msg = EditableFactory.newEditable(self.message)
        msg = cast('java.lang.String', "Yo yo yo, Dawg")
        toast.setText(msg)
        toast.show()


# Default to just logging the alert
Alert = AlertPrint

# Platform-specific alerts
if platform == "android":
    Alert = AlertToast

if platform == "macosx":
    try:    # Is Tkinter available?
        import Tkinter
        Alert = AlertTkinter
    except:
        pass
    
if platform == "linux":
    try:    # Is Tkinter available?
        import Tkinter
        Alert = AlertTkinter
    except:
        pass

if platform == "win":
    try:    # Is Tkinter available?
        import Tkinter
        Alert = AlertTkinter
    except:
        pass


if __name__ == "__main__":
    Alert("Hello, world!").show_alert()

