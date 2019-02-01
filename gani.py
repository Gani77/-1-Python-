# �� �������� ����
# ������ ������ �� ���� ������� :( ���� ��� ����� �������� ����� ��������� :) (��� � ��� normal)
# � ��,��� ��� ������ ������� ��������� ���� ��������� � ��� (� �� ��������� ���� � �����) 

import os,re
    
def adddir(dirname):   #easy 1
    a = os.path.join(os.getcwd(),dirname)
    try:
        os.mkdir(a)
        print("\nDirectory {} was succefully made".format(dirname))
    except FileExistsError:
        print("\nDirectory {} already exists".format(dirname))
    return " "


def deldir(dirname):     #easy 1
    a = os.path.join(os.getcwd(),dirname)
    try:
        os.rmdir(a)
        print("\nDirectory {} was succefully deleted".format(dirname))
    except FileExistsError:  
        print("\nDirectory {} doesn't exist".format(dirname))
    return " "


def viewDir(path = '.'):   #easy 2
    
    for i in os.listdir(path):
        if not (re.search('[.]+\w+',i)):
            print(i)
    return " "
