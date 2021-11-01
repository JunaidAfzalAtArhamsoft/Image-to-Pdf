from image_converter import ImageToPdf

if __name__ == '__main__':
    converter = ImageToPdf()

    converter.add_image('1.png')
    converter.add_image('images/free-flower-photos/flower-photo-1.jpg')
    converter.add_image('images/free-flower-photos/flower-photo-2.jpg')
    converter.add_image('images/free-flower-photos/flower-photo-3.jpg')
    converter.add_image('images/free-flower-photos/flower-photo-4.jpg')
    converter.add_image('images/free-flower-photos/flower-photo-5.jpg')
    converter.add_image('test_imag.png')

    converter.convert_images()

    file_name = input('With what file name you want to save it? ')
    converter.file_name_to_save = file_name

    converter.save_pdf_document()

    converter.view_document()
