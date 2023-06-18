from hume import HumeBatchClient
from hume.models.config import FaceConfig
from pprint import pprint
from hume import HumeStreamClient
import asyncio
import cv2

def capture_image():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Unable to access the camera.")
        return

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Failed to capture frame.")
        return

    # Save the image
    cv2.imwrite('captured_image.jpg', frame)
    print('Image captured!')

    # Release the VideoCapture object
    cap.release()

def findEmotion (result):
    max = 0
    for i in range(len)

while True:
    capture_image()

    async def main():
        client = HumeStreamClient("mPASmY2oLMgBm4X1UkE278lU6W8ILuOOvg7m8QFd5ADfucat")
        config = FaceConfig(identify_faces=True)
        async with client.connect([config]) as socket:
            result = await socket.send_file("captured_image.jpg")
            pprint(result['face']['predictions'][0]['emotions'][0])
            

    asyncio.run(main())