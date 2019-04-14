# iBuddy (PackHacks 2019)

## What it does

The application is divided into two parts.
1. Image analysis using tactile interface
2. Gesture controlled directional image analysis

## Workflow

- A user can interact with iBuddy using three buttons, Red, Green, and Yellow.
- The screen preview camera view and also shows the output of the analysis##### Use cases of buttons
- **Yellow Button**: Click a picture of the camera view
- **Red Button**: Answer No
- **Green Button**: Answer Yes

#### Tactile Interface for human face analysis

- User clicks a picture of image with a human face, using Yellow Button.
- The image is being sent to Azure Face API and we get the overall analysis in the returned json.
- User can listen to overall description of the image, and also see on the screen.
- iBuddy will then ask the user if he/she wants to know the emotion detected in the image.
- User can answer Yes/No using Green & Red Button.
- iBuddy will prompt the response accordingly.

<img src="https://user-images.githubusercontent.com/15925203/56093109-7dc7e800-5e92-11e9-9771-2d8d9ea119ab.jpg" alt="Input Image" style="width:400px;"/>

```
Description: A man looking at camera
Emotion: disgusted
Text: 
----------------------
Description: A man brushing his teeth in front of a mirror posing for the camera
Emotion: 
Text: 
----------------------
```

#### Tactile Interface for OCR

- User clicks a picture of image with using Yellow Button.
- The image is being sent to Azure Face API and we get the overall analysis in the returned json.
- User can listen to overall description of the image, and also see on the screen.
- iBuddy will then ask the user if he/she wants to know the text recognised in the image.
- User can answer Yes/No using Green & Red Button.
- iBuddy will prompt the response accordingly.


<img src="https://user-images.githubusercontent.com/15925203/56093170-33933680-5e93-11e9-8cf4-c4d7bbfd8a49.jpg" alt="Input Image" style="width:400px;"/>

```
Description: white board with black text
Text: NOTICE NO EATING OR DRINKING IN THIS AREA
----------------------
Description:  
Text: 
----------------------
```

#### Gesture Recognition

- The user can point to any of the four parts of the image and make a small circle with a finger pointed in that direction.
- Leap detects the gesture and iBuddy crops the image in that part 
- That part of the image is sent for analysis and appropriate results are returned.

Gesture Recognition
<img src="https://user-images.githubusercontent.com/15925203/56093163-0b0b3c80-5e93-11e9-9a50-58115d8f0429.jpg" alt="Input Image" style="width:400px;"/>

## How we built it

#### Technologies used
- Python 
- Leap Motion
- Raspberry-pi
- Azure
- Natural Language Processing
- Computer Vision
- Ngrok 
- Socket programming
- Python text-to-speech

## Challenges we ran into

- Setting up R-pi 
- Integrating leap motion

## Accomplishments that we are proud of

- Working product
- Successful gesture controlled directional analysis
- Low latency
- Good Accuracy

## What's next for iBuddy

- 360-degree image analysis
- Live video stream analysis
- Better physical device and integration

[GitHub](https://github.com/rikenshah/PackHacks2019)


