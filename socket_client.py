from websocket import create_connection
from websocket._exceptions import WebSocketConnectionClosedException


ra_current_ann = {}
hc_current_ann = {}
PORT='66666'
def listen_for_message():    
    ws=create_connection(f'ws://127.0.0.1:{PORT}')
    while True:
        data=ws.recv()
        if data:
            #Do something
            print(data)
        except WebSocketConnectionClosedException:
            listen_for_message()
            
if __name__=='__main__'    :
    listen_for_message()