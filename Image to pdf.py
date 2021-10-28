import os
import webbrowser
from PIL import Image


def image_to_pdf(im, file_name_to_save):
    """
    take input as image or list of images and convert them to pdf file with name file_name_to_save
    Parameters:
        im (Image):
        file_name_to_save (str):
    Returns:
        None
    """

    if len(im) > 0:

        im[0].save(file_name_to_save, save_all=True, append_images=images_to_convert[1:])
    else:
        print('Please Select at-least one image to convert it to pdf file..')


if __name__ == '__main__':

    file_name = 'my_pdf_file.pdf'
    images_to_convert = []
    while True:
        print('1-Enter Image to add in pdf\n'
              '2-Done and convert selected images to pdf\n'
              '3-Open pdf file\n'
              '0-Exit'
              )
        choice = input('Enter image with full path: ')
        if choice == '1':
            image_path = input('Enter image full path: ')

            try:
                image = Image.open(image_path)
                image = image.convert('RGB')
                images_to_convert.append(image)
            except FileNotFoundError:
                print("File don't exist on the specified path..\nKindly entered the correct path.")

        elif choice == '2':
            image_to_pdf(images_to_convert, file_name)

        elif choice == '3':

            if os.path.isfile(file_name):
                print('file is now being open in web-browser')
                webbrowser.open_new(file_name)
            else:
                print('File not exist')

        elif choice == '0':
            break
        else:
            print('Invalid choice')
