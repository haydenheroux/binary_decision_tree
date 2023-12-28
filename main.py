from tree.node import QuestionNode, AnswerNode

if __name__ == "__main__":
    root = QuestionNode(question="Is AD")
    root.false = AnswerNode(value=["Gwen"])
    melee = QuestionNode(question="Is Melee")
    melee.true = AnswerNode(value=["Camille", "Fiora", "Irelia", "Riven"])
    melee.false = AnswerNode(value=["Quinn"])
    root.true = melee

    print(root.traverse())