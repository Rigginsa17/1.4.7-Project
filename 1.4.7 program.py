import PIL
import os.path 

def logo(directory=None):
    # Open the files in the same directory as the Python script
    directory = os.path.dirname(os.path.abspath(__file__))  
    logo = os.path.join(directory, 'logo.jpg')
   
    new_directory = os.path.join(directory, 'modified')
    
    try:
        os.mkdir(new_directory)
    except OSError:
        pass 
    image_list, file_list = get_images(directory)  
    for img in range(len(image_list)):
        filename, filetype = file_list[img].split('.')
        new_image.paste(
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        student_img.paste(earth_small, (1162, 966), mask=earth_small) 