from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
values = np.array([0, 0, 0, 0, 0])

class Classmate:
    def __init__(self, name, section, fav_subject):
        self.name = name
        self.section = section
        self.fav_subject = fav_subject

    def introduce(self):
        msg = "Hi! I am " + self.name + " from " + self.section + ". My favorite subject is " + self.fav_subject + "."
        display(msg, target="displayArea", append=True)

c1 = Classmate("Aaron", "Sapphire", "English")
c2 = Classmate("Harvey", "Topaz", "Science")
c3 = Classmate("James", "Ruby", "Social Studies")
c4 = Classmate("Wayne", "Emerald", "PE")
c5 = Classmate("Euan", "Sapphire", "Math")

classmates_list = [c1, c2, c3, c4, c5]

def add_classmate(e):
    n = document.getElementById("nameInput").value
    s = document.getElementById("sectionInput").value
    f = document.getElementById("subjectInput").value

    if n == "" or s == "" or f == "":
        document.getElementById("displayArea").innerHTML = "PLS ADD SOMETHING"
        return

    new_one = Classmate(n, s, f)
    
    global classmates_list
    classmates_list += [new_one]

    document.getElementById("nameInput").value = ""
    document.getElementById("sectionInput").value = ""
    document.getElementById("subjectInput").value = ""

def show_list(e):
    document.getElementById("displayArea").innerHTML = ""

    for person in classmates_list:
        person.introduce()

def add_data(e):
    day = document.getElementById("day").value
    absence = int(document.getElementById("absences").value)

    index = list(days).index(day)
    values[index] = absence

    display("Successfully Submitted", target="out", append=False)

def show_graph(e):
    plt.figure()
    plt.plot(days, values, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    display(plt, target="out",)

img1= ["xmas.jpg"]
img2= ["intram.JPG"]
img3= ["class.JPG"]
img4= ["wag.JPG"]
tar="target"
for tar in tar:
    gal= document.getElementById("gallery")
    if gal:
        for img1 in img1:
                img_data = mpimg.imread(img1)
                plt.imshow(img_data)
                plt.axis('off')
                display(plt.gcf(), target="out1")
        for img2 in img2:
                img_data = mpimg.imread(img2)
                plt.imshow(img_data)
                plt.axis('off')
                display(plt.gcf(), target="out2")
        for img3 in img3:
                img_data = mpimg.imread(img3)
                plt.imshow(img_data)
                plt.axis('off')
                display(plt.gcf(), target="out3")
        for img4 in img4:
                img_data = mpimg.imread(img4)
                plt.imshow(img_data)
                plt.axis('off')
                display(plt.gcf(), target="out4")
    else:
         print("Not Here")