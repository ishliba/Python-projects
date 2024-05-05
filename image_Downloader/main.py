
import requests
import os

def get_extention(image_url: str) -> str:
    extentions = [".jpg",".jpeg",".png",".gif",".svg"]
    for ext in extentions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None):
    if ext:= get_extention(image_url):
        if folder:
            image_name = f"{folder}/{name}{ext}"
        else:
            image_name = f"{name}{ext}"
    else:
        raise Exception("Image extention could not be located....")

    #check if name already exists
    if os.path.isfile(image_name):
        raise Exception(" File name already exists ")

    #downloading image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"Downloaded: {image_name} successfully")
    except Exception as e:
        print(f"error {e}")

if __name__ == "__main__":
    input_url: str = input("enter a URL to download: ")
    input_name: str = input("what would you loke to name it?: ")

    print("downloading....")
    download_image(image_url=input_url, name=input_name, folder='images')



