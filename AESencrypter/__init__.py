import pyAesCrypt, sys, os
import pyautogui as py
import Tkinter as tk
from Tkinter import *

#window setup
def create():
    window = Tk()
    window.title("File Encrypt")

    encryptButton = Button(window,width=7, text="Encrypt" , bg='black', fg='green', command= encrypt)
    encryptButton.grid(column= 0, row= 0)


    decryptButton = Button(window,width=7,bg='black' , text="Decrypt", fg='green', command= decrypt)
    decryptButton.grid(column= 1, row= 0)

    closeButton = Button(window,width=7,bg='black',  text="Close", fg='green', command= quit)
    closeButton.grid(column= 1, row= 1)

    window.mainloop()


def getFilePath():
    path = py.prompt(text='Enter path to your file', title='File Path' , default='/base/filepath.(extension)')
    return path


def encrypt():
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    match=False

    filePathEncrypt = getFilePath()

    while match is False:
        password = py.password(text='Enter password:', title='Password', default='enter password', mask='*')

        passwordConfirm = py.password(text='Confirm password:', title='Password', default='confirm password', mask='*')

        if password == passwordConfirm:
            match =True
        else:
            py.prompt(text='Passwords did not match, please click ok and try enter password again.', title='Password')


    # Encrypt
    pyAesCrypt.encryptFile(filePathEncrypt , filePathEncrypt+".aes" , password, bufferSize)

    os.system('rm ' + filePath)

def decrypt():

    filePathDecrypt = getFilePath()

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    password = py.password(text='Enter password:', title='Password', default='enter password', mask='*')

    # get length of file Path
    pathLen = len(filePathDecrypt)

    # get range for string array
    endRange = pathLen - 3

    #get file path without aes extension
    fileWithout, empty =  os.path.splitext(filePathDecrypt)[0:endRange]

    # decrypt
    pyAesCrypt.decryptFile(filePathDecrypt, fileWithout , password,bufferSize)


    os.system('rm ' + filePathDecrypt)



def quit():
    window.destroy()


if __name__ == '__main__':
    create()