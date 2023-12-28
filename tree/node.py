from typing import ForwardRef, List, Union

QuestionNodeType = ForwardRef("QuestionNode")
AnswerNodeType = ForwardRef("AnswerNode")

class QuestionNode():
    def __init__(self, left: Union[QuestionNodeType, AnswerNodeType, None]=None, right: Union[QuestionNodeType, AnswerNodeType, None]=None, question=""):
        self.false = left
        self.true = right
        self.question = question

    def traverse(self) -> AnswerNodeType:
        selected = self.test()

        if isinstance(selected, AnswerNode):
            return selected

        return selected.traverse()
        

    def test(self) -> Union[QuestionNodeType, AnswerNodeType]:
        response = input(f"{self.question}? ")
        if response in ["y", "yes"]:
            return self.true
        elif response in ["n", "no"]:
            return self.false
        else:
            # Retry
            return self.test()

class AnswerNode():
    def __init__(self, value: List[str]):
        self.value = value
    
    def __str__(self):
        return f"{self.value}"