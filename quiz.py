answers = ["A","B","C","C","E","D","A","B","D"]
responses = ["A","B","C","C","E","D","A","C","B"]
if responses[-1]:
 answers[len(responses)-1]
 correct = True
else:
	correct = False

if not correct:
	del responses[-1]
	print("Sorry,please try last question again!")
elif len(responses)<len(answers):
	print("Quiz not complete!")
	correct = string(len(responses))
	print("You've got" + correct + "answers correct so far, please add an answer for th next question.")
else:
	print("Well done, you have completed the quiz!")