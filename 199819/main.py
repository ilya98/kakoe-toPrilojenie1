# Создание и запуск приложения, программирование интерфейса экранов и действий на них
# Здесь должен быть твой код
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box1 = BoxLayout(orientation='vertical' ,padding = 5, spacing = 8)
        txtStart = Label(text='Тест Руфье', size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inpName = TextInput(text='Введите ваше имя', halign='left', focus=False, multiline=False, size_hint=(.3, .07), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inpAge = TextInput(text='Введите ваш возраст', halign='left', focus=False, multiline=False, size_hint=(.3, .07), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnContinue = Button(text='Далее', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        def btnContinue_pressed():
            self.manager.current = 'scr2'
        btnContinue.on_press = btnContinue_pressed
        box1.add_widget(txtStart)
        box1.add_widget(inpName)
        box1.add_widget(inpAge)
        box1.add_widget(btnContinue)
        self.add_widget(box1)

class TimerTxt(Label):
    def __init__(self, time, **kwargs):
        super().__init__(**kwargs)
        self.done = False
        self.time = time
        self.current = 0
        text = 'Прошло секунд: ' + str(self.current)
    
    def countdown(self, done):
        self.current += 1
        self.text = ('Прошло секунд: ' + str(self.current))
        if self.current >= self.time:
            self.done = True
            return False
    
    def restart(self):
        self.done = False
        self.time = time
        self.current = 0
        self.start()
    
    def start(self):
        Clock.schedule_interval(self.countdown, 1)
    

class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box2 = BoxLayout(orientation='vertical' ,padding = 5, spacing = 8)
        txtPuls = Label(text='Замерьте пульс за 15 секунд.', size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnStartP = Button(text='Начать', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnContinue2 = Button(text='Далее', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        tmrPuls = TimerTxt(15, size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inpPuls = TextInput(text='Введите результат', halign='left', focus=False, multiline=False, size_hint=(.3, .08), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        def btnStartP_pressed():
            btnStartP.set_disabled(True)
            tmrPuls.start()
            Clock.schedule_once(btnContinue2_appear, 1)
        btnStartP.on_press = btnStartP_pressed
        def btnContinue2_pressed():
            self.manager.current = 'scr3'
        btnContinue2.on_press = btnContinue2_pressed
        def btnContinue2_appear(dt):
            box2.remove_widget(btnStartP)
            box2.add_widget(btnContinue2)
            return False
        box2.add_widget(txtPuls)
        box2.add_widget(tmrPuls)
        box2.add_widget(inpPuls)
        box2.add_widget(btnStartP)
        self.add_widget(box2)

class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box3 = BoxLayout(orientation='vertical' ,padding = 5, spacing = 8)
        txtPrisedania = Label(text='Выполните 30 приседаний за 45 секунд', size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        tmrPrisedania = TimerTxt(45, size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnStartPr = Button(text='Начать выполнять приседания', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnContinue3 = Button(text='Продолжить', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        def btnStartPr_pressed():
            btnStartPr.set_disabled(True)
            tmrPrisedania.start()
            Clock.schedule_once(btnContinue3_appear, 1)
        btnStartPr.on_press = btnStartPr_pressed
        def btnContinue3_pressed():
            self.manager.current = 'scr4'
        def btnContinue3_appear(dt):
            box3.remove_widget(btnStartPr)
            box3.add_widget(btnContinue3)
            return False
        btnContinue3.on_press = btnContinue3_pressed
        box3.add_widget(txtPrisedania)
        box3.add_widget(tmrPrisedania)
        box3.add_widget(btnStartPr)
        self.add_widget(box3)

class Screen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box4 = BoxLayout(orientation='vertical' ,padding = 5, spacing = 8)
        txtPuls2 = Label(text='В течении минуты измерьте пульс 2 раза:', size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnStartP2 = Button(text='Начать', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnEnd = Button(text='Завершить', size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        tmrPuls2_start = TimerTxt(15, size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        tmrPuls2_break = TimerTxt(30, size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        tmrPuls2_end = TimerTxt(15, size_hint=(.4, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inpResult = TextInput(text='Результат', halign='left', focus=False, multiline=False, size_hint=(.3, .08), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        inpResult_break = TextInput(text='Результат после отдыха', halign='left', focus=False, multiline=False, size_hint=(.3, .08), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        def btnStartP2_pressed():
            btnStartP2.set_disabled(True)
            tmrPuls2_start.start()
            Clock.schedule_once(P2_break, 5)
        btnStartP2.on_press = btnStartP2_pressed
        def P2_break():
            box4.remove_widget(tmrPuls2_start)
            box4.add_widget(tmrPuls2_break)
            tmrPuls2_break.start()
            Clock.schedule_once(P2_end, 5)
        def P2_end():
            box4.remove_widget(tmrPuls2_break)
            box4.add_widget(tmrPuls2_end)
            tmrPuls2_end.start()
        box4.add_widget(txtPuls2)
        box4.add_widget(tmrPuls2_start)
        box4.add_widget(inpResult)
        box4.add_widget(inpResult_break)
        box4.add_widget(btnStartP2)
        self.add_widget(box4)

class Screen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box5 = BoxLayout(orientation='vertical' ,padding = 5, spacing = 8)
        txtFinal = Label(text='text', size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        box5.add_widget(txtFinal)
        self.add_widget(box5)

class Test(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name = 'scr1'))
        sm.add_widget(Screen2(name = 'scr2'))
        sm.add_widget(Screen3(name = 'scr3'))
        sm.add_widget(Screen4(name = 'scr4'))
        sm.add_widget(Screen5(name = 'scr5'))
        return sm
    
app = Test()
app.run()