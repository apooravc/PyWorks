from flask import Flask, render_template
from random import randint

app = Flask(__name__)

def create_lists():
    front_list, middle_list, rear_list = [], [], []
    with open("insults.csv") as file:
        file_lines = file.readlines()
        for csv_line in file_lines:
            insult_list = csv_line.strip().split(",")
            front_list.append(insult_list[0])
            middle_list.append(insult_list[1])
            rear_list.append(insult_list[2])
    return front_list, middle_list, rear_list

front_list, middle_list, rear_list = create_lists()

def generate_insult():
    front_index = randint(0, len(front_list) - 1)
    middle_index = randint(0, len(middle_list) - 1)
    rear_index = randint(0, len(rear_list) - 1)
    insult = "{front} {middle} {rear}".format(front = front_list[front_index], middle = middle_list[middle_index], rear = rear_list[rear_index])
    return insult

@app.route("/")
def index():
    insult = "Thou {insult}!".format(insult = generate_insult())
    return render_template("index.html", insult = insult)
