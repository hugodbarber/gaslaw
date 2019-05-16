import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import tkMessageBox
from Tkinter import StringVar 
from Tkinter import OptionMenu
from gaslib import * #Remember to save gaslib.py in the same folder

#download_images()


def helpwindow():
    helpwindow = tk.Toplevel(app)
    helpwindow.geometry("350x250")
    title_label = tk.Label(helpwindow, text = "Help")
    help_label = tk.Label(helpwindow, text = "Help\n\n" + "1. Open the app\n" + "2. Select the law that you want to use\n" +
    "3. Select the variable that you would like to calculate\n" + "4. Enter the values for the other values\n" +
    "5. Press the calculate button\n" + "6. The answer will appear in the answer box\n" +
    "7. If an error message appears amend\n" +"Please type in the values for the calculator in the entry boxes\n" + "below but leave the entry box for what you\n" + 
    "are trying to find blank.\n" + "For example, if you are trying to find Pressure 1,\n" + "leave the Pressure 1 text box blank.\n", justify = tk.LEFT)
    title_label.pack()
    help_label.pack()
    helpwindow.mainloop()

class GasLawApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Gas Law Program')


        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        self.sub_title_font = tkfont.Font(family='Helvetica', size=12, slant="italic")
        self.text_font = tkfont.Font(family='Helvetica', size=10)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)        

        self.frames = {}
        for F in (Home, Boyleslaw, Charles, Lussac, Ideal):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
            frame = self.frames[page_name]
            frame.grid()


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        widget = tk.Label(self)
        widget.image = tk.PhotoImage(file="bgpic.gif")
        widget['image'] = widget.image   
        widget.grid(row = 0, column = 0)

##        widget2 = tk.Label(self)
##        widget2.image2 = tk.PhotoImage(file="balloon.gif")
##        widget2['image'] = widget2.image2   
##        widget2.place(relx=0.5, rely=0.6, anchor="center")

        label = tk.Label(self, text="GAS LAWS", font=controller.title_font)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button1 = tk.Button(self, text=u"Boyle's Law\n P\u2081V\u2081 = P\u2082V\u2082", command=lambda: controller.show_frame("Boyleslaw"))
        button2 = tk.Button(self, text=u"Charles Law\n V\u2081/T\u2081 = V\u2082/T\u2082", command=lambda: controller.show_frame("Charles"))
        button3 = tk.Button(self, text=u"Gay-Lussac's\n P\u2081/T\u2081 = P\u2082/T\u2082", command=lambda: controller.show_frame("Lussac"))
        button4 = tk.Button(self, text="Ideal gas Law\n PV = nRT", command=lambda: controller.show_frame("Ideal"))
        button5 = tk.Button(self, text="  Help  ", command=helpwindow)
        button1.place(relx=0.35, rely=0.3, anchor="center")
        button2.place(relx=0.45, rely=0.3, anchor="center")
        button3.place(relx=0.55, rely=0.3, anchor="center")
        button4.place(relx=0.65, rely=0.3, anchor="center")
        button5.place(relx=0.90, rely=0.2, anchor="center")
        label2 = tk.Label(self, text="The gas laws are the physical laws that describe the " +
        "properties of gases and are further explained by clicking one of the 4 links below.", justify=tk.LEFT, font=controller.sub_title_font)
        label2.place(relx=0.5, rely=0.2, anchor="center")


class Boyleslaw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        widget3 = tk.Label(self)
        widget3.image3 = tk.PhotoImage(file="bgpiclaw.gif")
        widget3['image'] = widget3.image3
        widget3.grid(row = 0, column = 0)

##        widget4 = tk.Label(self)
##        widget4.image4 = tk.PhotoImage(file="balloon.gif")
##        widget4['image'] = widget4.image4   
##        widget4.place(relx=0.5, rely=0.5, anchor="center")
        
        label = tk.Label(self, text="Boyle's Law", font=controller.title_font)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button = tk.Button(self, text="Home",command=lambda: controller.show_frame("Home"))
        button.place(relx=0.05, rely=0.1, anchor="center")

        def pvpv_option_changed(*args):
            print "Boyles: The user chose the value {}".format(pvpvvar.get())

        def pvpv():
                x_Result["text"] = ""
                p1 = p1_number_input.get()
                v1 = v1_number_input.get()
                p2 = p2_number_input.get()
                v2 = v2_number_input.get()
                x_Result["text"] = pvpvCalc(pvpvvar.get() ,p1, v1, p2, v2, x_Result)

        def getText():
             return BText()
        TEXT = getText()
        equation_Label = tk.Label(self, text=u"Equation: P\u2081V\u2081 = P\u2082V\u2082\n" + "Help\n\n" + "1. Select the variable you want to calculate\n" + "2. Input Kelvin for temperature\n" +
        "3. Don't put Information in the wrong box\n" + "4. Press the calculate button\n", justify = tk.LEFT)
        equation_Label.place(relx=0.2, rely=0.8, anchor="center")


                
        text_label = tk.Label(self, text = TEXT, justify = tk.LEFT, font=controller.text_font)
        text_label.place(relx=0.5, rely=0.25, anchor="center")
        headboycalc = tk.Label(self, text = 'Boyle\'s Law Calculator',justify = tk.LEFT)
        headboycalc.place(relx=0.2, rely=0.4, anchor = 'center')
        text_label2 = tk.Label(self, text = "Please select what you want to calculate from the drop down menu.", justify = tk.LEFT)
        text_label2.place(relx=0.2, rely=0.4, anchor="center")

        pvpvvar = StringVar(self)
        pvpvvar.set("p1") # default value
        pvpvvar.trace("w", pvpv_option_changed)

        w = OptionMenu(self, pvpvvar, "p1","v1", "p2", "v2")
        w.place(relx=0.4, rely=0.4, anchor="center")

        p1_Label = tk.Label(self, text="Pressure 1:")
        p1_Label.place(relx=0.12, rely=0.5, anchor="center")
        p1_number_input = tk.Entry(self)
        p1_number_input.place(relx=0.2, rely=0.5, anchor="center")

        v1_Label = tk.Label(self, text="Volume 1:")
        v1_Label.place(relx=0.32, rely=0.5, anchor="center")
        v1_number_input = tk.Entry(self)
        v1_number_input.place(relx=0.4, rely=0.5, anchor="center")

        p2_Label = tk.Label(self, text="Pressure 2:")
        p2_Label.place(relx=0.52, rely=0.5, anchor="center")
        p2_number_input = tk.Entry(self)
        p2_number_input.place(relx=0.6, rely=0.5, anchor="center")

        v2_Label = tk.Label(self, text="Volume 2:")
        v2_Label.place(relx=0.72, rely=0.5, anchor="center")
        v2_number_input = tk.Entry(self)
        v2_number_input.place(relx=0.8, rely=0.5, anchor="center")

        calc_button = tk.Button(self, text="Calculate", command = pvpv)
        calc_button.place(relx=0.45, rely=0.6, anchor="center")

        x_Label = tk.Label(self, text="Answer:")
        x_Label.place(relx=0.55, rely=0.6, anchor="center")
        x_Result = tk.Label(self)
        x_Result.place(relx=0.65, rely=0.6, anchor="center")

class Charles(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        widget3 = tk.Label(self)
        widget3.image3 = tk.PhotoImage(file="bgpiclaw.gif")
        widget3['image'] = widget3.image3
        widget3.grid(row = 0, column = 0)
        
        label = tk.Label(self, text="Charles Law", font=controller.title_font)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button = tk.Button(self, text="Home",command=lambda: controller.show_frame("Home"))
        button.place(relx=0.05, rely=0.1, anchor="center")

        def vtvt_option_changed(*args):
            print "Charles: The user chose the value {}".format(vtvtvar.get())

        def vtvt():
                x_Result["text"] = ""
                v1 = Cv1_number_input.get()
                t1 = Ct1_number_input.get()
                v2 = Cv2_number_input.get()
                t2 = Ct2_number_input.get()
                x_Result["text"] = vtvtCalc(vtvtvar.get() ,v1, t1, v2, t2, x_Result)

        def CgetText():
             return CText()
        CTEXT = CgetText()
        equation_Label = tk.Label(self, text=u"Equation: V\u2081/T\u2081 = V\u2082/T\u2082\n\n" + "1. Select the variable you want to calculate\n" + "2. Input Kelvin for temperature\n" +
        "3. Don't put Information in the wrong box\n" + "4. Press the calculate button\n", justify = tk.LEFT)
        equation_Label.place(relx=0.2, rely=0.8, anchor="center")
        text_label = tk.Label(self, text = CTEXT, justify = tk.LEFT)
        text_label.place(relx=0.5, rely=0.25, anchor="center")
        text_label2 = tk.Label(self, text = "Please select what you want to calculate from the drop down menu.", justify = tk.LEFT)
        text_label2.place(relx=0.2, rely=0.4, anchor="center")

        vtvtvar = StringVar(self)
        vtvtvar.set("v1") # default value
        vtvtvar.trace("w", vtvt_option_changed)

        w = OptionMenu(self, vtvtvar, "v1","t1", "v2", "t2")
        w.place(relx=0.4, rely=0.4, anchor="center")

        Cv1_Label = tk.Label(self, text="Volume 1:")
        Cv1_Label.place(relx=0.12, rely=0.5, anchor="center")
        Cv1_number_input = tk.Entry(self)
        Cv1_number_input.place(relx=0.2, rely=0.5, anchor="center")

        Ct1_Label = tk.Label(self, text="Temperature 1:")
        Ct1_Label.place(relx=0.32, rely=0.5, anchor="center")
        Ct1_number_input = tk.Entry(self)
        Ct1_number_input.place(relx=0.4, rely=0.5, anchor="center")

        Cv2_Label = tk.Label(self, text="Volume 2:")
        Cv2_Label.place(relx=0.52, rely=0.5, anchor="center")
        Cv2_number_input = tk.Entry(self)
        Cv2_number_input.place(relx=0.6, rely=0.5, anchor="center")

        Ct2_Label = tk.Label(self, text="Temperature 2:")
        Ct2_Label.place(relx=0.72, rely=0.5, anchor="center")
        Ct2_number_input = tk.Entry(self)
        Ct2_number_input.place(relx=0.8, rely=0.5, anchor="center")

        calc_button = tk.Button(self, text="Calculate", command = vtvt)
        calc_button.place(relx=0.45, rely=0.6, anchor="center")

        x_Label = tk.Label(self, text="Answer:")
        x_Label.place(relx=0.55, rely=0.6, anchor="center")
        x_Result = tk.Label(self)
        x_Result.place(relx=0.65, rely=0.6, anchor="center")

class Lussac(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        widget3 = tk.Label(self)
        widget3.image3 = tk.PhotoImage(file="bgpiclaw.gif")
        widget3['image'] = widget3.image3
        widget3.grid(row = 0, column = 0)
        
        label = tk.Label(self, text="Gay-Lussac's Law", font=controller.title_font)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button = tk.Button(self, text="Home",command=lambda: controller.show_frame("Home"))
        button.place(relx=0.05, rely=0.1, anchor="center")

        def ptpt_option_changed(*args):
            print "Lussac: The user chose the value {}".format(ptptvar.get())

        def ptpt():
                x_Result["text"] = ""
                p1 = Lp1_number_input.get()
                t1 = Lt1_number_input.get()
                p2 = Lp2_number_input.get()
                t2 = Lt2_number_input.get()
                x_Result["text"] = ptptCalc(ptptvar.get() ,p1, t1, p2, t2, x_Result)

        def LgetText():
             return LText()
        LTEXT = LgetText()
        equation_Label = tk.Label(self, text=u"Equation: P\u2081/T\u2081 = P\u2082/T\u2082\n\n" + "1. Select the variable you want to calculate\n" + "2. Input Kelvin for temperature\n" +
        "3. Don't put Information in the wrong box\n" + "4. Press the calculate button\n", justify = tk.LEFT)
        equation_Label.place(relx=0.2, rely=0.8 , anchor="center")
        text_label = tk.Label(self, text = LTEXT, justify = tk.LEFT)
        text_label.place(relx=0.5, rely=0.25, anchor="center")
        text_label2 = tk.Label(self, text = "Please select what you want to calculate from the drop down menu.", justify = tk.LEFT)
        text_label2.place(relx=0.2, rely=0.4, anchor="center")

        ptptvar = StringVar(self)
        ptptvar.set("p1") # default value
        ptptvar.trace("w", ptpt_option_changed)

        w = OptionMenu(self, ptptvar, "p1","t1", "p2", "t2")
        w.place(relx=0.4, rely=0.4, anchor="center")

        Lp1_Label = tk.Label(self, text="Pressure 1:")
        Lp1_Label.place(relx=0.12, rely=0.5, anchor="center")
        Lp1_number_input = tk.Entry(self)
        Lp1_number_input.place(relx=0.2, rely=0.5, anchor="center")

        Lt1_Label = tk.Label(self, text="Temperature 1:")
        Lt1_Label.place(relx=0.32, rely=0.5, anchor="center")
        Lt1_number_input = tk.Entry(self)
        Lt1_number_input.place(relx=0.4, rely=0.5, anchor="center")

        Lp2_Label = tk.Label(self, text="Pressure 2:")
        Lp2_Label.place(relx=0.52, rely=0.5, anchor="center")
        Lp2_number_input = tk.Entry(self)
        Lp2_number_input.place(relx=0.6, rely=0.5, anchor="center")

        Lt2_Label = tk.Label(self, text="Temperature 2:")
        Lt2_Label.place(relx=0.72, rely=0.5, anchor="center")
        Lt2_number_input = tk.Entry(self)
        Lt2_number_input.place(relx=0.8, rely=0.5, anchor="center")

        calc_button = tk.Button(self, text="Calculate", command = ptpt)
        calc_button.place(relx=0.45, rely=0.6, anchor="center")

        x_Label = tk.Label(self, text="Answer:")
        x_Label.place(relx=0.55, rely=0.6, anchor="center")
        x_Result = tk.Label(self)
        x_Result.place(relx=0.65, rely=0.6, anchor="center")

class Ideal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        widget3 = tk.Label(self)
        widget3.image3 = tk.PhotoImage(file="bgpiclaw.gif")
        widget3['image'] = widget3.image3
        widget3.grid(row = 0, column = 0)
        
        label = tk.Label(self, text="Ideal Gas Law", font=controller.title_font)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button = tk.Button(self, text="Home",command=lambda: controller.show_frame("Home"))
        button.place(relx=0.05, rely=0.1, anchor="center")

        def pvnrt_option_changed(*args):
            print "Ideal gas law: The user chose the value {}".format(pvnrtvar.get())

        def pvnrt():
                x_Result["text"] = ""
                p = Ip_number_input.get()
                v = Iv_number_input.get()
                n = In_number_input.get()
                t = It_number_input.get()
                x_Result["text"] = pvnrtCalc(pvnrtvar.get() ,p, v, n, t, x_Result)

        def IgetText():
             return IText()
        ITEXT = IgetText()
        equation_Label = tk.Label(self, text="Equation: PV = nRT using R = 8.314 J / mol K\n\n" + "1. Select the variable you want to calculate\n" + "2. Input Kelvin for temperature\n" +
        "3. Don't put Information in the wrong box\n" + "4. Press the calculate button\n", justify = tk.LEFT)
        equation_Label.place(relx=0.2, rely=0.8, anchor="center")
        text_label = tk.Label(self, text = ITEXT, justify = tk.LEFT)
        text_label.place(relx=0.5, rely=0.25, anchor="center")
        text_label2 = tk.Label(self, text = "Please select what you want to calculate from the drop down menu.", justify = tk.LEFT)
        text_label2.place(relx=0.2, rely=0.4, anchor="center")

        pvnrtvar = StringVar(self)
        pvnrtvar.set("P") # default value
        pvnrtvar.trace("w", pvnrt_option_changed)

        w = OptionMenu(self, pvnrtvar, "P", "V", "n", "T")
        w.place(relx=0.4, rely=0.4, anchor="center")

        Ip_Label = tk.Label(self, text="Pressure:")
        Ip_Label.place(relx=0.12, rely=0.5, anchor="center")
        Ip_number_input = tk.Entry(self)
        Ip_number_input.place(relx=0.2, rely=0.5, anchor="center")

        Iv_Label = tk.Label(self, text="Volume:")
        Iv_Label.place(relx=0.32, rely=0.5, anchor="center")
        Iv_number_input = tk.Entry(self)
        Iv_number_input.place(relx=0.4, rely=0.5, anchor="center")

        In_Label = tk.Label(self, text="Moles:")
        In_Label.place(relx=0.52, rely=0.5, anchor="center")
        In_number_input = tk.Entry(self)
        In_number_input.place(relx=0.6, rely=0.5, anchor="center")

        It_Label = tk.Label(self, text="Temperature:")
        It_Label.place(relx=0.72, rely=0.5, anchor="center")
        It_number_input = tk.Entry(self)
        It_number_input.place(relx=0.8, rely=0.5, anchor="center")

        calc_button = tk.Button(self, text="Calculate", command = pvnrt)
        calc_button.place(relx=0.45, rely=0.6, anchor="center")

        x_Label = tk.Label(self, text="Answer:")
        x_Label.place(relx=0.55, rely=0.6, anchor="center")
        x_Result = tk.Label(self)
        x_Result.place(relx=0.65, rely=0.6, anchor="center")

if __name__ == "__main__":
    app = GasLawApp()
    app.mainloop()
