import locale
import io
from PIL import Image

def getName(s):
    s = s.split()
    lname = s[0]
    fname = s[-1]
    return (lname, fname)
    
def compare(name):
    locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
    lname = getName(name)[0]
    fname = getName(name)[1]
    return locale.strxfrm(fname), locale.strxfrm(lname)

def sort_by_name(student_list):
    """
    Sort students list by name in Vietnamese alphabet
    """
    student_list.sort(key=lambda x: compare(x[1]))
    return student_list

def image_to_octet_string(image_path):
    with open(image_path, "rb") as image_file:
        return image_file.read()

def octet_string_to_image(octet_string):
    img = Image.open(io.BytesIO(octet_string))
    return img
