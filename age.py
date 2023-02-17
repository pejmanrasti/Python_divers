import cv2
from deepface import DeepFace

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Capture a single frame from the webcam
ret, frame = cap.read()

# Detect the age of the person in the frame using Deepface
detected_faces = DeepFace.analyze(frame, actions=["gender","age"])

# Extract the age of the first person in the list (if any)
age = detected_faces[0]["age"] if len(detected_faces)>0 else None

# Extract the gender of the first person in the list (if any)
gender = detected_faces[0]["gender"] if len(detected_faces)>0 else None

## Bucket the age
if int(age)>=13 and int(age)<=30:
    estimatedAge = 'less than 30 --> Need identification'
else:
    estimatedAge = 'more than 30'
# Print the age of the person
print("Predicted Age: ", age)
print("Category Age: ", estimatedAge)

# Print the gender of the person
print("Gender: ", gender)

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
