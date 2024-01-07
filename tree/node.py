from typing import ForwardRef, List, Optional, Union

QuestionNodeType = ForwardRef("QuestionNode")
AnswerNodeType = ForwardRef("AnswerNode")

class QuestionNode():
    def __init__(self, question, left: Optional[Union[QuestionNodeType, AnswerNodeType]]=None, right: Optional[Union[QuestionNodeType, AnswerNodeType]]=None):
        self.question = question
        self.false = left
        self.true = right

    def interactive_search(self) -> AnswerNodeType:
        questionOrAnswer: Union[QuestionNodeType, AnswerNodeType] = self.ask()

        if isinstance(questionOrAnswer, AnswerNode):
            return questionOrAnswer

        return questionOrAnswer.interactive_search()
        

    def ask(self) -> Union[QuestionNodeType, AnswerNodeType]:
        response = input(f"{self.question}? ")
        if response in ["y", "yes"]:
            return self.true
        elif response in ["n", "no"]:
            return self.false
        else:
            # Retry
            return self.ask()

class AnswerNode():
    def __init__(self, value: List[str]):
        self.value = value
    
    def __str__(self):
        return f"{self.value}"