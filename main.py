from controller import Controller
from model import Model
from view import View

model = Model()
view = View()
controller = Controller(view, model)
view.set_controller(controller)

if __name__ == "__main__":
    view.run()