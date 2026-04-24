from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from instr import *
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
from runner import Runner
from sits import Sits
from ruffier import test

bg = (0.80, 0.44, 0.6, 1)
Window.clearcolor = bg
btn_color = (0.99, 0.25, 0.3, 1)

#premade variable
'''age = 17
name = "linh"
p1 = 100
p2 = 160
p3 = 120 '''
def check_int(number):
    try:
        return int(number)
    except ValueError:
        try:
            return int(float(number))
        except:
            pass
    return False

class Main_Screen(Screen):
    def __init__(self, name = "main"):
        super().__init__(name = name)
        
        self.main_layout = BoxLayout(orientation = "vertical")

        main_label = Label(text = txt_instruction)
        self.btn = Button(text = "Start test", size_hint = (0.3, 0.2), pos_hint= {"center_x": 0.5, "center_y": 0.5})
        self.btn.on_press = self.move_1st
        self.btn.background_color = btn_color

        #line 1
        lbl_name = Label(text = "Enter your name", halign= "right")
        self.name_txt = TextInput()

        self.line1 = BoxLayout(orientation = "horizontal", size_hint=(0.8, None), height= "30sp")
        self.line1.add_widget(lbl_name)
        self.line1.add_widget(self.name_txt)
    #line2 for age input
    #add line 2 to main_layout

        #line 2
        lbl_age = Label(text = "[color=(.23, .53, .45] Enter your age [/color]", markup= True, halign="right")
        self.age_txt = TextInput() #int required

        self.line2 = BoxLayout(orientation = "horizontal", size_hint=(0.8, None), height= "40sp")
        self.line2.add_widget(lbl_age)
        self.line2.add_widget(self.age_txt)

        self.main_layout.add_widget(main_label)
        self.main_layout.add_widget(self.line1)
        self.main_layout.add_widget(self.line2)
        self.main_layout.add_widget(self.btn)


        self.add_widget(self.main_layout)


    def move_1st(self):
        #check if age is iint
        global name, age
        name = self.name_txt.text
        age = check_int(self.age_txt.text) #either be an int or false

        if age:
            if age > 7 and age < 17 :
                self.manager.transition.direction = "up"
                self.manager.current = "first"




    #other 3 move func to navigate to main
class First_Screen(Screen):
    def __init__(self, name = "first"):
        super().__init__(name = name)
        #timer
        self.counter = 0
        self.timer_text = Label(text = f"Seconds have passed:{self.counter}")

        self.first_layout = BoxLayout(orientation = "vertical")
        

        lbl_test1 = Label(text = txt_test1)
        self.btn = Button(text = "Start", size_hint = (0.3, 0.2), pos_hint= {"center_x": 0.5, "center_y": 0.5})
        self.btn.on_press = self.start_timing
        self.btn.background_color = btn_color

    #line 3
        lbl_pulse1 = Label(text = "Enter the result", halign= "right")
        self.pulse1_txt = TextInput()

        self.line3 = BoxLayout(orientation = "horizontal", size_hint=(0.8, None), height= "30sp")
        self.line3.add_widget(lbl_pulse1)
        self.line3.add_widget(self.pulse1_txt)


        self.first_layout.add_widget(lbl_test1)
        self.first_layout.add_widget(self.timer_text)
        self.first_layout.add_widget(self.line3)
        self.first_layout.add_widget(self.btn)

        self.add_widget(self.first_layout)
    
    def start_timing(self):
        Clock.schedule_interval(self.change_timer, 1)
    
    def change_timer(self, dt) :
        self.counter += 1
        self.timer_text.text = f"Seconds have passed:{self.counter}"
        if self.counter == 15:
            self.btn.text = "Continue"
            self.btn.on_press = self.move_2nd
            return False

    def move_2nd(self):
        first_pulse = check_int(self.pulse1_txt.text)
        if first_pulse :
            self.manager.transition.direction = "right"
            self.manager.current = "second"
        global p1
        p1 = first_pulse


class Second_Screen(Screen):
    def __init__(self, name = "second"):
        super().__init__(name = name)
        self.next_screen = False


        button = Button(text = "Move back to first")


    #line 4

        main_label_sits = Label(text = txt_sits)
        self.btn = Button(text = "Start", size_hint = (0.3, 0.2), pos_hint= {"center_x": 0.5, "center_y": 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        self.main_label_sits = Sits(3) 
        self.run = Runner(total=3, steptime= 1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)
        
        self.line_2 = BoxLayout()
        vlay = BoxLayout(orientation = "vertical", size_hint= (0.3, 1))
        vlay.add_widget(self.main_label_sits)

        self.line_2.add_widget(main_label_sits)
        self.line_2.add_widget(vlay)
        self.line_2.add_widget(self.run)


        self.main_layout = BoxLayout(orientation = "vertical")
        self.main_layout.add_widget(self.line_2)
        self.main_layout.add_widget(self.btn)

    
        self.add_widget(self.main_layout)
    
    def run_finished(self, instance, value) :
        self.btn.set_disabled(False)
        self.btn.text = "Continue" #change from starts to continue
        self.next_screen = True #allows user to the next screen



    def move_3rd(self):
        self.manager.transition.direction = "left"
        self.manager.current = "third"

    
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True) #prevent user from changing screens
            self.run.start()
            self.run.bind(value=self.main_label_sits.next) #change the label sits accordingly
        else:
            self.manager.current = "third"





class Third_Screen(Screen):
    def __init__(self, name = "third"):
        super().__init__(name = name)
        self.fourth_layout = BoxLayout(orientation = "vertical")
        main_label_test3 = Label(text = txt_test3)

        #input pulse before rest
        lbl_pulse_before_rest = Label(text= "Enter your pulse")
        self.pulse_before_rest = TextInput()

        self.before_rest = BoxLayout(orientation = "horizontal", size_hint=(0.8, None), height= "30sp")
        self.before_rest.add_widget(lbl_pulse_before_rest)
        self.before_rest.add_widget(self.pulse_before_rest)

        lbl_pulse_rest = Label(text= "Rest")
        self.pulse_rest = TextInput()
        self.rest = BoxLayout(orientation = "horizontal", size_hint=(0.8, None), height= "40sp")
        self.rest.add_widget(lbl_pulse_rest)
        self.rest.add_widget(self.pulse_rest)

        self.btn = Button(text = "Finalize", size_hint = (0.3, 0.2), pos_hint= {"center_x": 0.5, "center_y": 0.5})
        self.btn.on_press = self.finalize
        

        self.fourth_layout.add_widget(main_label_test3)
        self.fourth_layout.add_widget(self.before_rest)
        self.fourth_layout.add_widget(self.rest)
        self.fourth_layout.add_widget(self.btn)
        

        self.add_widget(self.fourth_layout)
        


    def finalize(self):
        self.manager.transition.direction = "left"
        self.manager.current = "result"
        global p2, p3
        p2 = check_int(self.pulse_before_rest.text)
        p3 = check_int(self.pulse_rest.text)


class Result_Screen(Screen):
    def __init__(self, name="result"):
        super().__init__(name=name)
        btn = Button(text = "redo", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        btn.on_press=(self.move_main)

        self.result_layout = BoxLayout(orientation = "vertical", padding=8, spacing =8)
        

        self.instr = Label(text = " ")
        self.result_layout.add_widget(self.instr)

        self.result_layout.add_widget(btn)

        self.add_widget(self.result_layout)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n" + test(p1, p2, p3, age)
       

    def move_main(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main"


class My_App(App):
    def build(self):
        screen_manager = ScreenManager()
        #create screen
        self.main_screen = Main_Screen()
        self.first_screen = First_Screen()

        self.second_screen = Second_Screen()
        self.third_screen = Third_Screen()
        self.result_screen = Result_Screen()



        screen_manager.add_widget(self.main_screen)
        screen_manager.add_widget(self.first_screen)
        screen_manager.add_widget(self.second_screen)
        screen_manager.add_widget(self.third_screen)
        screen_manager.add_widget(self.result_screen)
        


        screen_manager.current = "main"
        #link event
        return screen_manager



my_app = My_App()
my_app.run()