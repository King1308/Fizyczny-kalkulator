from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import os
import sys


def toStp(r):
    n = r[:3]
    answer = 0
    if n == "[da":
        answer = 1
    else:
        n = r[:2]
    if n == "[n":
        answer = -9
    elif n == "[µ":
        answer = -6
    elif n == "[m":
        answer = -3
    elif n == "[c":
        answer = -2
    elif n == "[d":
        answer = -1
    elif n == "[h":
        answer = 2
    elif n == "[h":
        answer = 2
    elif n == "[k":
        answer = 3
    elif n == "[M":
        answer = 6
    elif n == "[G":
        answer = 9
    return(answer)


def aFm():
    nul = 0
    aFmFText = ui.aFmFInp.text()
    if not aFmFText:
        nul += 1
    aFmSText = ui.aFmSInp.text()
    if not aFmSText:
        nul += 1
    aFmMText = ui.aFmMInp.text()
    if not aFmMText:
        nul += 1
    if nul != 1:
        msg = QMessageBox()
        msg.setWindowTitle("Eror")
        msg.setText("Musi byc podane 2 znaczenia")
        msg.exec_()
        sys.exit()
    try:
        if not aFmFText:
            st = toStp(ui.aFmSType.currentText())
            aFmSValue = float(aFmSText) if st == 0 else float(
                aFmSText) * (10 ** st)
            mt = toStp(ui.aFmMType.currentText())
            aFmMValue = float(
                aFmMText) * 10 ** -3 if mt == 0 else float(aFmMText) * (10 ** mt) * (10 ** -3)
            aFmFValue = aFmSValue * aFmMValue
            answer = f'''          F
a = ------
         m
Z tego wynika że:

F = a*m

Rozwiązamy:

F = {aFmSValue}*{aFmMValue}
{aFmFValue} = {aFmSValue}*{aFmMValue}
F = {aFmFValue}

Odpowiedż:
Siła potrebna pry masie w {aFmMValue}kg dla przyskorenia w {aFmSValue}m/s²:
{aFmFValue}N'''
            ui.aFmOutp.setText(answer)
            ui.aFmFInp.setText(str(aFmFValue))
        elif not aFmSText:
            ft = toStp(ui.aFmFType.currentText())
            aFmFValue = float(aFmFText) if ft == 0 else float(
                aFmFText) * (10 ** ft)
            mt = toStp(ui.aFmMType.currentText())
            aFmMValue = float(
                aFmMText) * 10 ** -3 if mt == 0 else float(aFmMText) * (10 ** mt) * 10 ** -3
            aFmSValue = aFmFValue / aFmMValue
            answer = f'''          F
a = ------
         m

Rozwiązamy:

a = {aFmFValue}/{aFmMValue}
{aFmSValue} = {aFmFValue}/{aFmMValue}
a = {aFmFValue}

Odpowiedż:
Pryspieszenie pry sile w {aFmFValue}N dla ciała z masią w {aFmMValue}kg będzie:
{aFmSValue}m/s²'''
            ui.aFmOutp.setText(answer)
            ui.aFmSInp.setText(str(aFmSValue))
        elif not aFmMText:
            ft = toStp(ui.aFmFType.currentText())
            aFmFValue = float(aFmFText) if ft == 0 else float(
                aFmFText) * (10 ** ft)
            st = toStp(ui.aFmSType.currentText())
            aFmSValue = float(aFmSText) if st == 0 else float(
                aFmSText) * (10 ** st)
            aFmMValue = (aFmFValue / aFmSValue)
            answer = f'''          F
a = ------
         m

Z tego wynika że:

m = F/a

Rozwiązamy:

m = {aFmFValue}/{aFmSValue}
{aFmMValue} = {aFmFValue}/{aFmSValue}
m = {aFmMValue}

Odpowiedż:
Masa ciała do którego nadali siłe w {aFmFValue}N i otrzymali przyspieszenie w {aFmSValue}m/s²:
{aFmMValue}kg'''
            ui.aFmOutp.setText(answer)
            ui.aFmMInp.setText(str(aFmMValue))
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Eror")
        msg.setText("Wszystki znaczenia musza byc podani w cyfrach")
        msg.exec_()
        sys.exit()
    except Exception as e:
        print(e)


def initialize():
    global app, ui
    app = QtWidgets.QApplication([])
    if getattr(sys, 'frozen', False):
        ui = uic.loadUi(os.path.join(sys._MEIPASS, "files/ui.ui"))
        aFmPixmap = QPixmap(os.path.join(sys._MEIPASS, "files/aFm.svg"))
    else:
        ui = uic.loadUi("ui.ui")
        aFmPixmap = QPixmap('aFm.svg')
    ui.setFixedSize(500, 620)
    ui.setWindowTitle("Fizyczny kalkulator")
    ui.aFmPic.setPixmap(aFmPixmap)
    ui.aFmBtn.clicked.connect(aFm)
    ui.show()
    app.exec()


if __name__ == "__main__":
    initialize()
