import os
import json
import datetime
from datetime import datetime
from pywebio import start_server
from pywebio.input import *
from pywebio.input import input
import Data_database

def bmi():
    data = input_group("User info",[
    input("Approved by:" , placeholder='Your name',name = 'name'),
    input("Serial number:", placeholder='LVI## - 2004####', name ='serialNumber'),
    input("Board number:", placeholder='SBC - ####', name ='boardNumber'),
    radio("Pi-heatsink", options=['Approved', 'Declined'], name = 'pi'),
    radio("Electrical connections", options=['Approved', 'Declined'], name='crimp'),
    radio("Lanyard", options=['Approved', 'Declined'], name='lanyard'),
    radio("Screen torqued@2N-m", options=['Approved', 'Declined'], name='screen'),
    radio("Scratch revision", options=['Approved', 'Declined'], name='scratch'),
    radio("Flus keypad", options=['Approved', 'Declined'], name='keypad'),
    radio("Camera", options=['Approved', 'Declined'], name='camera'),
    radio("Keylock w/locktite", options=['Approved', 'Declined'], name='keylock'),
    radio("Arrow buttons /Left up", options=['Approved', 'Declined'], name='buttons'),
    radio("Seal on edges", options=['Approved', 'Declined'], name='seal'),
    radio("Microphone", options=['Approved', 'Declined'], name='mic'),
    radio("Tamper switch", options=['Approved', 'Declined'], name='tamper'),
    radio("Fan polarity/Pdot=(-)", options=['Approved', 'Declined'], name='fan'),
    radio("power_wire power wire", options=['Approved', 'Declined'], name='power_wire'),
    radio("Ground nut", options=['Approved', 'Declined'], name='groundNut'),
    radio("Sticker/bot-left", options=['Approved', 'Declined'], name='sticker'),
    radio("W2 jumper placed", options=['Approved', 'Declined'], name='w2'),
    radio("Videcall", options=['Approved', 'Declined'], name='ScreenResolution'),
    radio("QR code", options=['Approved', 'Declined'], name='qr'),
    radio("Correct icons", options=['Approved', 'Declined'], name='icons'),
    radio("Fob reads", options=['Approved', 'Declined'], name='fobRead'),
    radio("Volume correct", options=['Approved', 'Declined'], name='volume'),
    radio("Is the unit connected to Balena?", options=['Approved', 'Declined'], name='balena'),
    radio("Does the fob number match in Balena?", options=['Approved', 'Declined'], name='fobnumber'),
    radio("Is this a reworked unit?", options=['Yes', 'No'], name='rework'),

    #This part is to add buttons and interactable widgets like buttons
    actions('QC items', [
    {'label': 'Save results', 'value': "saved"},
    ], name='action', help_text='actions'),
    ])
    #print(data["name"], data["serialNumber"], data["boardNumber"])
    if data["rework"] == "Yes":
        filename = data["serialNumber"]+ '-R' + '.json'
    else:
        filename = data["serialNumber"] + '.json'
    folderID= '1cEMsQQe4Doz1CUlyP6pP9DWiwucy69AJ'
    
    if data['action'] == "saved":
        data["Date"] = datetime.now().strftime("%m:%d:%y")
        hoy = datetime.now().strftime("%m:%d:%y")
        with open(f"/home/pi/Desktop/2000_QC_capturing_QC.com/data/{filename}", 'w') as fp:
            json.dump(data, fp, indent=4)
            
        #Save data into database
        Data_database.log_data(data['name'],hoy,data['serialNumber'],data['boardNumber'],data['pi'],data['crimp'],data['lanyard'],data['screen'],data['scratch'],data['keypad'],data['camera'],data['keylock'],data['buttons'],data['seal'],data['mic'],data['tamper'],data['fan'],data['power_wire'],data['groundNut'],data['sticker'],data['w2'],data['ScreenResolution'],data['qr'],data['icons'],data['fobRead'],data['volume'],data['balena'],data['fobnumber'],data['rework'])

"""
def save(data,filename,folderID):
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    upload_file_list = [filename]
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    #print(file_list)
    file_list = os.listdir()
    for file1 in file_list:
        if filename in file1:
            #print(f"This:{filename}")
            if data['rework'] == 'No':
                return print ('File is a duplicate')
    for upload_file in upload_file_list:
        gfile = drive.CreateFile({'parents': [{'id':folderID}]})
        gfile.SetContentFile(upload_file)
        gfile.Upload()
    start_server(bmi, port=8986)
"""
if __name__ == '__main__':
    start_server(bmi, port=8986, host = "10.0.0.211") 