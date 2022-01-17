import fpdf
import webbrowser
import os


class ImageToPdf:
    """
    Image To pdf Converter
    """
    def __init__(self):
        self.images = []
        self.pdf = fpdf.FPDF()
        self._file_name_to_save = ''

    @property
    def file_name_to_save(self):
        return self._file_name_to_save

    @file_name_to_save.setter
    def file_name_to_save(self, file_name):
        if os.path.isfile('{}.pdf'.format(file_name)):
            print(f'File with name "{file_name}" already exist.\nSelect operation:\n')
            operation = input('1- Override the file\n2- Save with other name\nSelect: ')
            if operation == '1':
                self._file_name_to_save = '{}.pdf'.format(file_name)
                print('\nFile is override.')
            elif operation == '2':
                file_name = input('Enter different file name: ')
                self.file_name_to_save = file_name
        else:
            self._file_name_to_save = '{}.pdf'.format(file_name)

    def add_image(self, path):
        """
        Message: Add image to list
        Parameters:
             path (str): Full address of image
        Returns:
            None
        """
        if os.path.isfile(path):
            self.images.append(path)
        else:
            print('No such file exist.')

    # ################################################################################# #

    def convert_images(self):
        """
        Convert the selected list of images to pdf file.
        Parameters:
            self
        Returns:
            None
        """

        print('Your document will be ready in few seconds.\nPlease Wait..')
        y = 10
        change_y = 0
        count = 0
        for image in self.images:
            if count % 2 == 0:
                self.pdf.add_page()
                y = 10
                change_y = 0
            self.pdf.image(image, 15, y + change_y, 180, (180*56)/100)
            change_y += int((180*60)/100)
            count += 1

        print('Processing Complete.\nYou can check it.')

    # ################################################################################# #

    def save_pdf_document(self):
        """
        Message: Save pdf document with provided file name.
        Parameters:
            self
        Returns:
            None
        """
        self.pdf.output(self.file_name_to_save, 'F')

    def view_document(self):
        """
        Message: Open the saved pdf document
        Parameters:
            self:
        Returns:
            None
        """
        if os.path.isfile(self.file_name_to_save):
            webbrowser.open(self.file_name_to_save)
        else:
            print('No such File Exist...')
