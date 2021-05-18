from datetime import datetime

def hello():
    return "Hello!👋 How are you"

def who():
    return "I am ZiXu_bot, created by the awesome ZiXu."

def time():
    now = datetime.now()
    date_time = now.strftime("Date: %d/%m/%y, Time: %H:%M:%S")
    return date_time

def love():
    return "I love you baby~~~~~~~~<3"

def response(input_text):
    user_message = str(input_text).lower()
    responses_dict = {
        ("hello","hi","sup"):hello,
        ("who are you", "who are you?"):who,
        ("time","time?"): time,
        ("bernice", "baby"): love,
    }
    def checker(user_message, responses_dict):
        for keys in responses_dict.keys():
            if user_message in keys:
                func = responses_dict.get(keys)
                return func()
        return False
    return checker(user_message, responses_dict)