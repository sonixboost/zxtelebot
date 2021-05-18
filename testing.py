from datetime import datetime

""" def check(input):
    responses_dict = {
        "hello":helloo,
        "who are you":'who',
        "time": 'time'
    }
    func = responses_dict.get(input, lambda: False)
    print(func())

def helloo():
    return ('hi')

# print(check('who are you'))
print(check('hello'))
# print(check('time'))
# print(check('sad')) """
"""
def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello","hi","sup"):
        return ("Hello!👋 How are you")

    if user_message in ("who are you", "who are you?"):
        return "I am ZiXu_bot, created by the awesome ZiXu."

    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("Date: %d/%m/%y, Time: %H:%M:%S")

        return date_time
"""

def foo():
    global a
    a = 10
    return 11
print(foo())
print(a)