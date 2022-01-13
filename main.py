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
    radio("Pi-heatsink installed", options=['Approved', 'Declined'], name = 'pi'),
    radio("Electrical connections", options=['Approved', 'Declined'], name='crimp'),
    radio("Lanyard installed", options=['Approved', 'Declined'], name='lanyard'),
    radio("Screen torqued@2N-m", options=['Approved', 'Declined'], name='screen'),
    radio("Scratch revision", options=['Approved', 'Declined'], name='scratch'),
    radio("Flus keypad", options=['Approved', 'Declined'], name='keypad'),
    radio("Camera installed/functional", options=['Approved', 'Declined'], name='camera'),
    radio("Keylock w/locktite", options=['Approved', 'Declined'], name='keylock'),
    radio("Arrow buttons /Left up", options=['Approved', 'Declined'], name='buttons'),
    radio("Seal on edges installed", options=['Approved', 'Declined'], name='seal'),
    radio("Microphone installed/functional", options=['Approved', 'Declined'], name='mic'),
    radio("Tamper switch installed", options=['Approved', 'Declined'], name='tamper'),
    radio("Fan polarity/Pdot=(-)", options=['Approved', 'Declined'], name='fan'),
    radio("SMP5 power wire gage/spade terminals", options=['Approved', 'Declined'], name='power_wire'),
    radio("Ground nut placed", options=['Approved', 'Declined'], name='groundNut'),
    radio("Sticker/bot-left", options=['Approved', 'Declined'], name='sticker'),
    radio("W2 jumper placed", options=['Approved', 'Declined'], name='w2'),
    radio("Videcall functional", options=['Approved', 'Declined'], name='ScreenResolution'),
    radio("QR code feature functional", options=['Approved', 'Declined'], name='qr'),
    radio("Correct icons", options=['Approved', 'Declined'], name='icons'),
    radio("Fob reads", options=['Approved', 'Declined'], name='fobRead'),
    radio("Volume correct", options=['Approved', 'Declined'], name='volume'),
    radio("Is the unit connected to Balena?", options=['Approved', 'Declined'], name='balena'),
    radio("Does the fob number match in Balena?", options=['Approved', 'Declined'], name='fobnumber'),
    radio("Is this a reworked unit? Approved = yes", options=['Approved', 'Declined'], name='rework'),

    radio("Is the SMP5 dip switch locked with glue?", options=['Approved', 'Declined'], name='dipSwitch'),
    radio("Is the Motion Sensor installed?", options=['Approved', 'Declined'], name='motionSensor'),
    radio("Is the hidrophobic cloth placed by speakers /mic?", options=['Approved', 'Declined'], name='cloth'),
    radio("Have the yellow /brown card reader wires been removed?", options=['Approved', 'Declined'], name='readerWires'),
    radio("Have the connectors been locked with hot glue?", options=['Approved', 'Declined'], name='hotGlue'),
    radio("Is the screen protector placed firmly with resin?", options=['Approved', 'Declined'], name='resin'),
    radio("Have the wires connected to the up/down buttons been secured with crimps?", options=['Approved', 'Declined'], name='buttonCrimps'),
    radio("Have the buttons been torqued correctly?", options=['Approved', 'Declined'], name='buttonTorque'),
    radio("Is the heat sink on the SMP5 secured with loctite?", options=['Approved', 'Declined'], name='loctiteSink'),
    radio("Is the unit packed in a box with a plastic bag around it?", options=['Approved', 'Declined'], name='packed'),
    radio("Is the accessory bag attached? (Keys,Cloth,Bolts,Washers)", options=['Approved', 'Declined'], name='accessories'),

    #This part is to add buttons and interactable widgets like buttons
    actions('QC items', [
    {'label': 'Save results', 'value': "saved"},
    ], name='action', help_text='actions'),
    ])
    
    # Upload a file and save to server
    photos = input_group("pictures",[file_upload(label = 'Exterior and interior photos from unit',
                                                 placeholder = 'Choose file', multiple = True,name='photos')])
    filename = data['serialNumber']
    with open("/home/pi/Desktop/2000_QC_capturing_QC.com/data/pictures/{0}.jpeg".format(filename), "wb") as file:
        file.write(photos['photos'][0]['content'])
        
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
        Data_database.log_data(data['name'],hoy,data['serialNumber'],data['boardNumber'],
                               data['pi'],data['crimp'],data['lanyard'],data['screen'],
                               data['scratch'],data['keypad'],data['camera'],data['keylock'],
                               data['buttons'],data['seal'],data['mic'],data['tamper'],
                               data['fan'],data['power_wire'],data['groundNut'],data['sticker'],
                               data['w2'],data['ScreenResolution'],data['qr'],data['icons'],
                               data['fobRead'],data['volume'],data['balena'],data['fobnumber'],
                               data['rework'],data['dipSwitch'],data['motionSensor'],data['cloth'],
                               data['readerWires'],data['hotGlue'],data['resin'],data['buttonCrimps'],
                               data['buttonTorque'],data['loctiteSink'],data['packed'],data['accessories'])

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