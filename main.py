from multiprocessing import Process, Manager
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
from text_recognize_api_call import text_recognize
import sys
import pyttsx3
from gpiozero import Button

class ButtonPressed(Exception): pass

def main():
    
    p_face_detect = Process(target=face_detect, args = [end_result])
    p_image_analyze = Process(target=image_analyze, args = [end_result])
    p_text_recognize = Process(target=text_recognize, args = [end_result])
    p_face_detect.start()
    p_image_analyze.start()
    p_text_recognize.start()
    p_face_detect.join()
    p_image_analyze.join()
    p_text_recognize.join()
    
    button_green = Button(17)
    button_red = Button(15)
    engine.say(end_result["description"])
    engine.runAndWait()
    print(end_result)

    if end_result["emotion"]:
        engine.say("A face is detected, do you want to know the emotion?")
        engine.runAndWait()
        while True:
            button_green.when_pressed = emotion_yes_pressed
            button_red.when_pressed = no_pressed
    elif end_result["text"]:
        engine.say("Image has some text, do you want to listen?")
        engine.runAndWait()
        while True:
            button_green.when_pressed = text_yes_pressed
            button_red.when_pressed = no_pressed


def emotion_yes_pressed():
    engine.say(end_result["emotion"])
    engine.runAndWait()
    raise ButtonPressed


def text_yes_pressed():
    engine.say(end_result["text"])
    engine.runAndWait()
    raise ButtonPressed


def no_pressed():
    raise ButtonPressed


if __name__=='__main__':
    global end_result
    global engine
    manager = Manager()
    engine = pyttsx3.init()
    end_result = manager.dict()
    end_result['description'] = ''
    end_result['text'] = ''
    end_result['emotion'] = ''

    main()