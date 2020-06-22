#This script draws in a live video
import cv2

cap = cv2.VideoCapture(0)


# Automatically grab width and height from video feed
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# We're using // here because in Python // allows for int classical division,
# because we can't pass a float to the cv2.rectangle function

# Coordinates for Rectangle
x = width//2
y = height//2

# Width and height
w = width//4
h = height//4

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Draw a rectangle on stream

    cv2.rectangle(frame, (x, y), (x+w, y+h), color=(255,100,100),thickness= 4)

    # Display the resulting frame
    cv2.imshow('frame', frame)

   # This command let's us quit with the "q" button on a keyboard.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
