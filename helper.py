import locale
import io
import re
import controller
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

def validate_student_id(student_id):
    student_list = controller.get_students_list()
    id_list = [student[0] for student in student_list]
    regex = r'^\d{8}$'
    if re.match(regex, student_id) and int(student_id) not in id_list:
        return True
    else:
        return False

def validate_date(date_string):
    regex = r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$'
    if re.match(regex, date_string):
        return True
    else:
        return False

# if __name__ == '__main__':
#     print(validate_student_id('19000470'))
#     print(validate_student_id('1a900040'))