from enum import Enum
import pygame
import struct


# SQUARE = 0
# CROSS = 1
# CIRCLE = 2
# TRIANGLE = 3
# LEFT_SHOULDER_BUTTON = 4
# RIGHT_SHOULDER_BUTTON = 5
# LEFT_TRIGGER = 6
# RIGHT_TRIGGER = 7

class XBoxButtonValues(Enum):

    DESCEND = 0
    ASCEND = 1
    CLOSE_CLAW = 2
    OPEN_CLAW = 3

    DESCEND_OFF = 20
    ASCEND_OFF = 21
    CLOSE_CLAW_OFF = 22
    OPEN_CLAW_OFF = 23

    TURBO = 11
    TOGGLE_LIGHTS = 12

    LEFT_ON = 13
    RIGHT_ON = 14
    FORWARD_ON = 15
    BACKWARDS_ON = 16
    HAT_MOVEMENT_OFF = 17

class Controller(object):

    socket = None
    controller = None
    axis_data = None
    button_data = None
    hat_data = None


    def init(self, socket):
        # Initialize pygame joystick

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        self.socket = socket

    def listen(self):
        """Listen for events to happen"""

        while True:
            for event in pygame.event.get():
                # if event.type == pygame.JOYAXISMOTION:
                #     self.process_axis_data(round(event.value, 2))
                if event.type == pygame.JOYBUTTONDOWN:
                    self.update_pi(self.process_down_button_data(event.button))
                elif event.type == pygame.JOYBUTTONUP:
                    self.update_pi(self.process_up_button_data(event.button))
                elif event.type == pygame.JOYHATMOTION:
                    self.update_pi(self.process_hat_data(event.value))

    def update_pi(self, message):
        message = struct.pack('i', message)
        self.socket.send(message)

    # @staticmethod
    # def process_axis_data(axis_value):
    #     if axis_value > 0.1:
    #         print(axis_value)
    #     if axis_value < -0.1:
    #         print(axis_value)

    @staticmethod
    def process_down_button_data(button_value):
        return button_value

    @staticmethod
    def process_up_button_data(button_value):
        return button_value + 20

    @staticmethod
    def process_hat_data(hat_values):
        if hat_values == (0, 1):
            print(XBoxButtonValues.LEFT_ON.value)
            return XBoxButtonValues.FORWARD_ON.value
        elif hat_values == (0, -1):
            return XBoxButtonValues.BACKWARDS_ON.value
        elif hat_values == (-1, 0):
            return XBoxButtonValues.LEFT_ON.value
        elif hat_values == (1, 0):
            return XBoxButtonValues.RIGHT_ON.value
        else:
            return XBoxButtonValues.HAT_MOVEMENT_OFF.value


