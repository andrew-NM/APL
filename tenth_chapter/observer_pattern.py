class Subject:
    def __init__(self):
        self.observers = []
    
    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, message):
        for o in self.observers:
            o.update(message)

class Observer:
    def update(self, message):
        print(f"Received update {message}")

subject = Subject()
obs1 = Observer()
obs2 = Observer()

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Update available!")