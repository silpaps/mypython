class Vscode:
    def compile(self):
        print("compile using Vscode")
    def execute(self):
        print("execute using vscode")
    def debug(self):
        print("debug using Vscode")
class Pycharm:
    def compile(self):
        print("compile using Pycharm")
    def execute(self):
        print("execute using Pycharm")
    def debug(self):
        print("debug using Pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)
