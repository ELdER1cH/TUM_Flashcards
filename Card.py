class Card:   
    def __init__(self,course,question,answer):
        self.course = course
        self.question = question
        self.answer = answer
        self.topic = ""
        
    def __init__(self,course, topic,question,answer) -> None:
        self.course = course
        self.topic = topic
        self.question = question
        self.answer = answer
        
        
        
    def __str__(self) -> str:
        return f"Course: {self.course}\nTopic: {self.topic}\nQuestion: {self.question}\nAnswer: {self.answer}\n"
    
    def printQuestion(self):
        print(self.question)
    
    def printAnswer(self):
        print(self.answer)