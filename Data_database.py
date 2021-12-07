import sqlite3

def log_data(name,hoy,serialNumber,boardNumber,pi,crimp,lanyard,screen,scratch,keypad,camera,keylock,buttons,seal,mic,tamper,fan,power_wire,groundNut,sticker,w2,ScreenResolution,qr,icons,fobReads,volume,balena,fobnumber,rework):
    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    try:
        # Create table
        cur.execute('''CREATE TABLE logs (name text, date text, serial_number text,  board_number text, pi text, crimps 
        text, lanyard text, screen text, scratch text, keypad text, camera text, keylock text, buttons text, seal text, microphone text, tamper_switch text, fan text, power_wire text, ground_nut text, sticker text, W2_jumper text, screen_resolution text,QR_code_read text,icons text, fob_reads text,volume text, balena text,fob_number text,rework text)''')
    except:
        print("Table existed")
    # The qmark style used with executemany():
    lang_list = [
        (name,hoy,serialNumber,boardNumber,pi,crimp,lanyard,screen,scratch,keypad,camera,keylock,buttons,seal,mic,tamper,fan,power_wire,groundNut,sticker,w2,ScreenResolution,qr,icons,fobReads,volume,balena,fobnumber,rework),
    ]
    cur.executemany("INSERT INTO logs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", lang_list)

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

if __name__ == "__main__":
    log_data()