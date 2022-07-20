from State import *


class Transition:

    def __init__(self, input_label: str, output_label: str, input_state: State, output_state: State):
        self.input_label = input_label
        self.output_label = output_label
        self.input_state = input_state
        self.output_state = output_state
