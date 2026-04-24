
# program with three screens, switching to the third screen occurs by timer
# the timer is enabled in the on_enter method of the second screen, i.e. immediately after the user has entered this screen
# see line 58
 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

time_to_read = 5
long_txt = """Use these tips to increase your reading speed:\n
1. Do not pronounce the readable text.\n
If you already have a habit of pronouncing, practice reading and simultaneously singing one note with closed lips.\n 
2. Learn to grasp several words at once.\n
Practice by glancing at the text. Without moving your gaze, close your eyes and recall what you have read.\n 
3. Get your gaze moving from top to bottom.\n
Don't look back at what you've already read. Practice reading narrow columns of text.\n
You can help yourself by moving a sheet of paper over the text so that it covers the top of the page. Accelerate the movement of the sheet.\n
4. Concentrate on reading.\n
Read long texts. Remove distractions. Look for books that will captivate you. """

# class for neatly displaying long text on a small scrolling screen
# you can read more in the documentation for the first lesson
class ScrollLabel(ScrollView):
    def __init__(self, ltext, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text=ltext, markup=True, size_hint_y=None, font_size='20sp', halign='left', valign='top')
        self.label.bind(size=self.resize)
        self.add_widget(self.label)

    def resize(self, *argv):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=10)
        box.add_widget(Label(text="Try to read the text in " + str(time_to_read) + " second(s)"))
        btn_next = Button(text="Start", on_press=self.next)
        box.add_widget(btn_next)
        self.add_widget(box) 

    def next(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = 'showtext' 

class ShowText(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(padding=10)
        box.add_widget(ScrollLabel(long_txt, size_hint_x=0.8, pos_hint={'center_x':0.5})) 
        self.add_widget(box)
    
    def on_enter(self):
        print("kk")
        Clock.schedule_once(self.next, time_to_read)

    def next(self, dt):
        print(dt, "seconds passed ")
        self.manager.current = 'last' 

class LastScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Time!")) 

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='1'))
        sm.add_widget(ShowText(name='showtext'))
        sm.add_widget(LastScr(name='last'))
        return sm

app = MyApp()
app.run()
showclock.py
