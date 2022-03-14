from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
import re




Window.size = (350, 550)

class CalWidget(Widget):
    
    def clear(self):
        self.ids.input.text = "0"
    
    def back(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        self.ids.input.text = expression
    
    def result(self):
        expression = self.ids.input.text
        try:
            self.ids.input.text = str(eval(expression))
        except:
            self.ids.input.text = "ERREUR"
            
    def pressed(self, number):
        expression = self.ids.input.text
        if "ERREUR" in expression:
            expression = ""
            
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{number}"
        else:
            self.ids.input.text = f"{expression}{number}"
    
    
    def signs(self, sign):
        expression = self.ids.input.text
        self.ids.input.text = f"{expression}{sign}"
        
    
    def positive_negative(self):
        expression = self.ids.input.text
        
        if "-" in expression:
            self.ids.input.text = f"{expression.replace('-', '')}"
        else:
            self.ids.input.text = f"-{expression}"
            
    def dot(self):
        expression = self.ids.input.text
        num_list = re.split("\+|\*|/|-|%", expression)
        
        if ("+" in expression or "-" in expression or "/" in expression or "*" in expression or "%" in expression) and "." not in num_list[-1]:
            expression = f"{expression}."
            self.ids.input.text = expression
            
        
        elif "." in expression:
            pass
        
        else:
            expression = f"{expression}."
            self.ids.input.text = expression
            
               
            

class CalculatorApp(App):
    def build(self):
        return CalWidget()
        
    
    
    
CalculatorApp().run()