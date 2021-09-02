question_prompts=["what are colors of apple \n (a) red/green \n (b) yellow \n (c) orange\n \n",
                  "what are the colors of banana \n (a) magenta \n(b) blue\n(c) yellow \n\n",
                  "what colors are strawberries \n (a) rose \n (b) red\n (c) pink \n\n"
                  ]
class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
questions=[Question(question_prompts[0],"a"),
           Question(question_prompts[1],"c"),
           Question(question_prompts[2],"b")
          ]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("you got",score,"/",len(questions),"are correct")
run_test(questions)

