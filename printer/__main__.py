from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("picture.jpg") 
          
        #Angle given
        #img = img.rotate(180) 
          
         #Saved in the same relative location
        img.save("story.jpg")
    except IOError:
        print("Filename JPG Not found")
        pass
  
if __name__ == '__main__':
    main()
