import face_recognition
import sys

def load_and_encode_image(image_path):
    """
    Load an image file and encode the face(s) found in the image.
    """
    try:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            return encodings[0]  # Return the first face found
        else:
            print(f"No faces found in {image_path}")
            return None
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def compare_faces(image_path1, image_path2):
    """
    Compare the faces in two images and print whether they match.
    """
    encoding1 = load_and_encode_image(image_path1)
    encoding2 = load_and_encode_image(image_path2)

    if encoding1 is None or encoding2 is None:
        print("Face encoding failed for one or both images.")
        return

    # Compare the faces
    results = face_recognition.compare_faces([encoding1], encoding2)
    
    if results[0]:
        return "Success"
    else:
        return "Failed"
