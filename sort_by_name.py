import locale

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