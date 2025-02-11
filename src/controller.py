import inputs

class Controller:
    def __init__(self):
        self.controller = inputs.devices.gamepads[0]

    def get_button_status(self):
        events = inputs.get_gamepad()
        button_status = {}
        for event in events:
            if event.ev_type == 'Key':
                button_status[event.code] = event.state
            elif event.ev_type == 'Absolute' and event.code == 'ABS_Z':  # ABS_Z is the LeftTrigger
                button_status['LeftTrigger'] = event.state
        return button_status

    def close(self):
        pass  # No close method needed for the inputs library