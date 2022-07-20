from Transition import *


class FST:

    def __init__(self):
        self.states = []
        self.transitions = []
        self.outStrings = ["FAIL"]

    def getInitial(self):

        for state in self.states:
            if state.isInitial:
                return state

    def add_state(self, state_name, isFinal, isInitial):
        self.states.append(State(state_name, isFinal, isInitial))

    def add_transition(self, input_label: str, output_label: str, input_state: str, output_state: str):

        in_state = None
        out_state = None

        for state in self.states:
            if state.state_name == input_state:
                in_state = state
            if state.state_name == output_state:
                out_state = state

        self.transitions.append(Transition(input_label, output_label, in_state, out_state))

    def add_set_transition(self, inputset: str, input_state: str, output_state: str):

        for char in inputset:
            self.add_transition(char, char, input_state, output_state)

    def parse_input(self, state: State, input_str: str, output_str: str):

        lambda_transition = self.getTransition(state, 'λ')

        if len(input_str) == 0:

            if len(lambda_transition) == 0:

                if state.isFinal:
                    if 'FAIL' in self.outStrings:
                        self.outStrings.clear()

                    self.outStrings.append(output_str)
                    return output_str
                else:
                    return 'FAIL'

            elif len(lambda_transition) != 0:

                for t in lambda_transition:
                    self.parse_input(t.output_state, '',
                                     output_str + '' if t.output_label == 'λ' else output_str + t.output_label)

        elif len(input_str) != 0:

            notLambda_transition = self.getTransition(state, input_str[0])

            if len(notLambda_transition) == 0 and len(lambda_transition) == 0:

                return 'FAIL'

            elif len(notLambda_transition) != 0 and len(lambda_transition) == 0:

                for t in notLambda_transition:
                    self.parse_input(t.output_state, input_str[1:],
                                     output_str + '' if t.output_label == 'λ' else output_str + t.output_label)

            elif len(notLambda_transition) == 0 and len(lambda_transition) != 0:

                for t in lambda_transition:
                    self.parse_input(t.output_state, input_str,
                                     output_str + '' if t.output_label == 'λ' else output_str + t.output_label)

            elif len(notLambda_transition) != 0 and len(lambda_transition) != 0:

                all_tran = notLambda_transition + lambda_transition

                for t in all_tran:

                    if t in lambda_transition:
                        self.parse_input(t.output_state, input_str,
                                         output_str + '' if t.output_label == 'λ' else output_str + t.output_label)

                    elif t in notLambda_transition:
                        self.parse_input(t.output_state, input_str[1:],
                                         output_str + '' if t.output_label == 'λ' else output_str + t.output_label)

        return self.outStrings

    def getTransition(self, state: State, char: str):

        tran = []

        for transition in self.transitions:

            if transition.input_label == char and transition.input_state == state:
                tran.append(transition)

        return tran

    def printStates(self):

        for s in self.states:
            print(s.state_name)

    def printTran(self):
        for t in self.transitions:
            print(t.input_state.state_name, t.input_label, t.output_label, t.output_state.state_name)
