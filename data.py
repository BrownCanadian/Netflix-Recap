from tkinter import Image
import pygame
from bs4 import BeautifulSoup
import requests



file_handle = open('ViewingActivity.csv','r')
file_handle.readline()
shows=[]
time=[]
show_to_duration={}
count = 0
time_secs=[]
shows_key=[]
def collect_data():
    global count
    for l in file_handle:
        count+=1
        show= l.split(',')[4]
        tim = l.split(',')[2]
        shows.append(show)
        time.append(tim)
    
        
def to_seconds(timestr):
    seconds= 0
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part, 10)
    return seconds

def show():
    index=0
    trailer= "(Trailer)"
    Trailer= "Trailer"
    typ=""
    
    for i in shows:
        
        show = i
        if "_hook_" in i:
            
            show= i.split("_")[0]
            
        elif trailer in i:
            show= i.split('(')[0]
        elif "Trailer" in i:
            show = i.split(':')[-1]
        elif":" in i:
            show = i.split(':')[0]
            
            
        if ("Season" in show) and ("Trailer" not in show):
            show = i.split(":")[0]
            
        show=show.strip()   
        

        
        
        if show in show_to_duration:
            show_to_duration[show]+=to_seconds(time[index])
        else:
            show_to_duration[show]=to_seconds(time[index])
        index+=1   
            
            

def sort():
    for key in show_to_duration:
        time_secs.append(show_to_duration[key])
        shows_key.append(key)
    sort_orders = sorted(show_to_duration.items(), key=lambda x: x[1], reverse=True)
   
    return sort_orders
  

def top_charts():
    
    order = sort()
    l =  len(order)
    a = []
    if l==0:
        # print("You only watched one thing for now, and here it is: ")
        # print(order[0][0])
        a.append(order[0][0])
    elif l<4 :
        # print("Your top three are the only three you watched: ")
        count=1
        for i in order:
            print('#',count,': ', i[0])
            count+=1
            a.append(i[0])
    else:
        # print("From all the shows, your top watches were: ")
        for i in range(0,3):
            # print('#',i+1,': ', order[i][0])
            a.append(order[i][0])
    return a
            

def time_to_sec(time):
    tt_list = time.split(':')
    hours_to_sec = int(tt_list[0])*3600
    minutes_to_sec = int(tt_list[1])*60
    seconds_to_sec = int(tt_list[2])
    total = seconds_to_sec + minutes_to_sec + hours_to_sec


    return total 

def sec_to_hours(sec):
    hour = sec//60 + (sec % 60>0)
    return hour  
def total_hours(file_name):
    to = 0
    file_handle = open('ViewingActivity.csv','r')
    file_handle.readline() 
    for i in file_handle:
        time = i.split(',')[2]
        a = time_to_sec(time)
        to+=a

    final_total = sec_to_hours(to)
    
    return final_total  



# def get_Image(t):
#     url = "https://www.google.com/search?q="+t+"&rlz=1C1CHBF_enCA929CA929&sxsrf=APq-WBsM5de8Red8IbfVHPfCYaivuSlYAQ:1647380931925&source=lnms&tbm=isch&sa=X&ved=2ahUKEwij9IaajMn2AhVBIjQIHfE6D9kQ_AUoAXoECAIQAw&biw=1536&bih=656&dpr=1.25"
#     result = requests.get(url).text
#     doc = BeautifulSoup(result,"html.parser")
#     main_div = doc.find_all(class_="mJxzWe")
#     # main_div = doc.find_all(class_= "mJxzWe")
#     print("Hello: ", doc)
#     # print("URL IS: ", url)
#     # images = []
#     # for img in main_div:
#     #     print(img)
#     #     print(" ")
#     # print(images)


def main():
    a = total_hours("ViewingActivity.csv") 
    print("Total Hours: ", a)
    collect_data()
    show()
    sort()
    l = top_charts()
    print(l)

    
#TODO:
#  - Display a window(800*800) DONE
#  - Color Pallete(decide)
#  - Display text
#  - Download Image 
#  - Display Image

###URL




main()

    
pygame.init()
font_head = pygame.font.SysFont("Bebas Neue",50)
font_text = pygame.font.SysFont("Times New Roman",20)
font_int = pygame.font.SysFont("Bebas Neue",50)
def display_headings(text,x,y):
    sc_text = font_head.render(text, True , (0,0,0))
    surface.blit(sc_text, [x,y])
def display_text(text,x,y):
    sc_text = font_int.render(text, True , (0,0,0))
    surface.blit(sc_text, [x,y])
def display_topcharts(list):
    if len(list)>0:
        first = 50
        for i in list:
            first+=40
            sc_text = font_text.render(i, True , (255, 217, 125))
            surface.blit(sc_text, [24,first])



displaywidth = 600
displayheight = 300
surface = pygame.display.set_mode((displaywidth, displayheight))
while True:
    surface.fill((238, 96, 85))
    display_headings("Top Watches:",20,20)
    display_topcharts(top_charts())
    display_headings("Hrs Watched: ",20,240)
    display_text(str(total_hours("ViewingActivity.csv")),260,240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()




