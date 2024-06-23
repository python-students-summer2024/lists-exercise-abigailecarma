import datetime
import os

def make_text_file():
    if not os.path.isdir("data"):
        os.makedirs("data")

    if not os.path.isfile("data/mood_diary.txt"):
        file = open("data/mood_diary.txt", encoding="utf-8", mode="w")
        file.close()


def read_text_file():
    date_today = str(datetime.date.today())
    file = open("data/mood_diary.txt", encoding="utf-8", mode="r")
    lines = file.readlines()
    file.close()
    for l in lines:
        if date_today in l:
            print("Sorry, you have already entered your mood today.")
            return False
    return True


def stored_mood():
    while True:
        user_mood = input("What's your current mood? ").lower()
        if user_mood in ["happy", "relaxed", "apathetic", "sad", "angry"]:
            break
    
    if user_mood == "happy":
        return 2
    elif user_mood == "relaxed":
        return 1
    elif user_mood == "apathetic":
        return 0
    elif user_mood == "sad":
        return -1
    elif user_mood == "angry":
        return -2


def edit_text_file():
    date_today = str(datetime.date.today())
    file = open("data/mood_diary.txt", encoding="utf-8", mode="a")
    file.write(f"{date_today}: {stored_mood()}\n")
    file.close()


def diagnosing():
    file = open("data/mood_diary.txt", encoding="utf-8", mode="r")
    num_entries = file.readlines()
    file.close()
    if len(num_entries) >= 7:
        mood_num = []
        for entry in num_entries[-7:]:
            just_num = int(entry.split(": ")[-1])
            mood_num.append(just_num)

        avg_mood = round(sum(mood_num) / len(mood_num))
        if avg_mood == 2:
            avg_diagnosis = "happy"
        elif avg_mood == 1:
            avg_diagnosis = "relaxed"
        elif avg_mood == 0:
            avg_diagnosis = "apathetic"
        elif avg_mood == -1:
            avg_diagnosis = "sad"
        elif avg_mood == -2:
            avg_diagnosis = "angry"

        happy_num = 0
        sad_num = 0
        apathetic_num = 0

        for mood in mood_num:
            if mood == 2:
                happy_num += 1
            elif mood == -1:
                sad_num += 1
            elif mood == 0:
                apathetic_num += 1

        if happy_num >= 5:
            diagnosis = "manic"
        elif sad_num >= 4:
            diagnosis = "depressive"
        elif apathetic_num >= 6:
            diagnosis = "schizoid"
        else:
            diagnosis = avg_diagnosis

        print(f"Your diagnosis: {diagnosis}!") 


def assess_mood():
    make_text_file()
    if read_text_file():
        edit_text_file()
        diagnosing()
