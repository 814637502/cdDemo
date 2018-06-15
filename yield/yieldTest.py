__author__ = 'sunyawei'



def getgussPsychologist():
    print("how do you feel today?")
    while 1:
        answer = (yield)
        if answer:
            if "good" in answer:
                print("your anser is "+answer+"   so i do,it's a nice day")
            elif "bad" in answer:
                print("oh my babby ,give you a hug")
            else:
                print("what do you say ?")



a = getgussPsychologist()
a.next()
a.send("im good")



def test(lists=[]):
    lists.append(1)
    for a in lists:
        print(a)

test([])
test([])
test()
test()