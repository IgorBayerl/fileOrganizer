import time
import os
import json
import shutil
from datetime import datetime
from pathlib import Path
from time import gmtime, strftime

class FileOrganizer:
     
    def move_file(self, filename):
        if filename != 'fileOrganizer.ico':
            i = 1
            extension = 'noname'
            new_name = filename
            try:
                file_Name ,extension = os.path.splitext(filename)
                print(file_Name)
            except Exception :
                extension = 'noname'

            folder_destination_path = self.extensions_folders[extension]

            now = datetime.now()
            year = now.strftime("%Y")

            folderOperation = os.getcwd()

            year_exists = False
            for folder_name in os.listdir(self.extensions_folders[extension]):
                if folder_name == year:
                    folder_destination_path = self.extensions_folders[extension] + "/" +year
                    year_exists = True
                    
            if not year_exists:
                os.mkdir(self.extensions_folders[extension] + "/" + year)
                folder_destination_path = self.extensions_folders[extension] + "/" + year

            file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
            while file_exists:
                i += 1
                new_name = os.path.splitext(folderOperation + '/' + filename)[0] + str(i) + os.path.splitext(folderOperation + '/' + filename)[1]
                new_name = new_name.split("/")[1]
                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
            src = folderOperation + "/" + filename

            new_name = folder_destination_path + "/" + new_name
            os.rename(src, new_name)

    def organize(self):
        #constroi array com arquivos da pasta
        files = [
            filename for filename in os.listdir('.')
                if os.path.isfile(filename) and any(filename.lower().endswith(ext.lower()) for ext in self.extensions_folders)
        ]

        print(files)
        for filename in files:
            self.move_file(filename)

    extensions_folders = {
    #No name
        'noname' : "C:/Users/playb/Documents/Uncategorized",
    #Audio
        '.aif' : "C:/Users/playb/Music",
        '.cda' : "C:/Users/playb/Music",
        '.mid' : "C:/Users/playb/Music",
        '.midi' : "C:/Users/playb/Music",
        '.mp3' : "C:/Users/playb/Music",
        '.mpa' : "C:/Users/playb/Music",
        '.ogg' : "C:/Users/playb/Music",
        '.wav' : "C:/Users/playb/Music",
        '.wma' : "C:/Users/playb/Music",
        '.wpl' : "C:/Users/playb/Music",
        '.m3u' : "C:/Users/playb/Music",
    #Text
        '.txt' : "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
        '.doc' : "C:/Users/playb/Documents/DocumentosDeTexto/Word",
        '.docx' : "C:/Users/playb/Documents/DocumentosDeTexto/Word",
        '.odt ' : "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
        '.pdf': "C:/Users/playb/Documents/DocumentosDeTexto/PDF",
        '.rtf': "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
        '.tex': "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
        '.wks ': "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
        '.wps': "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
        '.wpd': "C:/Users/playb/Documents/DocumentosDeTexto/TextFiles",
    #Video
        '.3g2': "C:/Users/playb/Videos",
        '.3gp': "C:/Users/playb/Videos",
        '.avi': "C:/Users/playb/Videos",
        '.flv': "C:/Users/playb/Videos",
        '.h264': "C:/Users/playb/Videos",
        '.m4v': "C:/Users/playb/Videos",
        '.mkv': "C:/Users/playb/Videos",
        '.mov': "C:/Users/playb/Videos",
        '.mp4': "C:/Users/playb/Videos",
        '.mpg': "C:/Users/playb/Videos",
        '.mpeg': "C:/Users/playb/Videos",
        '.rm': "C:/Users/playb/Videos",
        '.swf': "C:/Users/playb/Videos",
        '.vob': "C:/Users/playb/Videos",
        '.wmv': "C:/Users/playb/Videos",
    #Images
        '.ai': "C:/Users/playb/Pictures",
        '.bmp': "C:/Users/playb/Pictures",
        '.gif': "C:/Users/playb/Pictures",
        '.ico': "C:/Icons",
        '.jpg': "C:/Users/playb/Pictures",
        '.jpeg': "C:/Users/playb/Pictures",
        '.png': "C:/Users/playb/Pictures",
        '.ps': "C:/Users/playb/Pictures",
        '.psd': "C:/Users/playb/Pictures",
        '.svg': "C:/Users/playb/Pictures/SVG",
        '.tif': "C:/Users/playb/Pictures",
        '.tiff': "C:/Users/playb/Pictures",
        '.CR2': "C:/Users/playb/Pictures",
    #Internet
        # '.asp': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.aspx': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.cer': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.cfm': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.cgi': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.pl': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.css': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.htm': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.js': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.jsp': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.part': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.php': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.rss': "C:/Users/playb/Desktop/kalle/Other/Internet",
        # '.xhtml': "C:/Users/playb/Desktop/kalle/Other/Internet",
    #Compressed
        '.7z': "C:/Users/playb/Compressed",
        '.arj': "C:/Users/playb/Compressed",
        '.deb': "C:/Users/playb/Compressed",
        '.pkg': "C:/Users/playb/Compressed",
        '.rar': "C:/Users/playb/Compressed",
        '.rpm': "C:/Users/playb/Compressed",
        '.tar.gz': "C:/Users/playb/Compressed",
        '.z': "C:/Users/playb/Compressed",
        '.zip': "C:/Users/playb/Compressed",
    #Disc
        '.bin': "C:/DiscImgs",
        '.dmg': "C:/DiscImgs",
        '.iso': "C:/DiscImgs",
        '.toast': "C:/DiscImgs",
        '.vcd': "C:/DiscImgs",
    #Data
        # '.csv': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.dat': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.db': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.dbf': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.log': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.mdb': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.sav': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.sql': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.tar': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.xml': "C:/Users/playb/Desktop/kalle/Programming/Database",
        # '.json': "C:/Users/playb/Desktop/kalle/Programming/Database",
    #Executables
        '.apk': "C:/Executables/AndroidAPKs",
        '.bat': "C:/Executables",
        '.com': "C:/Executables",
        '.exe': "C:/Executables",
        '.EXE': "C:/Executables",
        '.gadget': "C:/Executables",
        '.jar': "C:/Executables",
        '.wsf': "C:/Executables",
        '.msi' : "C:/Executables",
    #Fonts
        # '.fnt': "C:/Users/playb/Desktop/kalle/Other/Fonts",
        # '.fon': "C:/Users/playb/Desktop/kalle/Other/Fonts",
        # '.otf': "C:/Users/playb/Desktop/kalle/Other/Fonts",
        # '.ttf': "C:/Users/playb/Desktop/kalle/Other/Fonts",
    #Presentations
        '.key': "C:/Users/playb/Documents/Presentations",
        '.odp': "C:/Users/playb/Documents/Presentations",
        '.pps': "C:/Users/playb/Documents/Presentations",
        '.ppt': "C:/Users/playb/Documents/Presentations",
        '.pptx': "C:/Users/playb/Documents/Presentations",
    #Programming
        # '.c': "C:/Users/playb/Desktop/kalle/Programming/C&C++",
        # '.class': "C:/Users/playb/Desktop/kalle/Programming/Java",
        # '.dart': "C:/Users/playb/Desktop/kalle/Programming/Dart",
        # '.py': "C:/Users/playb/Desktop/kalle/Programming/Python",
        # '.sh': "C:/Users/playb/Desktop/kalle/Programming/Shell",
        # '.swift': "C:/Users/playb/Desktop/kalle/Programming/Swift",
        # '.html': "C:/Users/playb/Desktop/kalle/Programming/C&C++",
        # '.h': "C:/Users/playb/Desktop/kalle/Programming/C&C++",
    #Spreadsheets
        # '.ods' : "C:/Users/playb/Desktop/kalle/Text/Microsoft/Excel",
        # '.xlr' : "C:/Users/playb/Desktop/kalle/Text/Microsoft/Excel",
        # '.xls' : "C:/Users/playb/Desktop/kalle/Text/Microsoft/Excel",
        # '.xlsx' : "C:/Users/playb/Desktop/kalle/Text/Microsoft/Excel",
    #System
        # '.bak' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.cab' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.cfg' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.cpl' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.cur' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.dll' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.dmp' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.drv' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.icns' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.ico' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.ini' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.lnk' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        
        # '.sys' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
        # '.tmp' : "C:/Users/playb/Desktop/kalle/Text/Other/System",
}


FO = FileOrganizer()
FO.organize()


# pyinstaller -w -F fileOrganizer.py