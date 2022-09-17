import adhawkapi
import adhawkapi.frontend
import cv2


def main():
    api = adhawkapi.frontend.FrontendApi()
    api.start(connect_cb=on_connect, disconnect_cb=on_disconnect)

    aruco_dictionary = cv2.aruco.DICT_5X5_50
    screen_size = (0.345, 0.195)  # in meters
    marker_size = 0.03  # in meters
    marker_ids = [0, 1, 2, 3]
    markers_pos = [[0.0, 0.12], [0.27, 0.12], [0.0, 0.0], [0.27, 0.0]]

    api.register_screen_board(*screen_size, aruco_dictionary, marker_ids,
                            [[pos[0], pos[1], marker_size] for pos in markers_pos])

    api.start_screen_tracking()

    # Enabling data streams
    api.register_stream_handler(adhawkapi.PacketType.GAZE_IN_SCREEN, handler)
    api.set_stream_control(adhawkapi.PacketType.GAZE, 60)


    # Terminate communication
    api.shutdown()    

def on_connect(error):
    if not error:
        print('Connected to AdHawk Backend Service')

def on_disconnect(error):
    print('Disconnected from AdHawk Backend Service')

def handler(*data):
    print(data)
    timestamp, xpos, ypos = data

if __name__ == "__main__":
    main()
