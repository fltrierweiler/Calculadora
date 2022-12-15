

class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model
    
    def on_button_click(self, caption):
        result = self.model.calculate(caption)
        self.view.value_var.set(result)
    
    def run_view(self):
        self.view.run()
