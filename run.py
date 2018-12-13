# Run the command line server

import rasa_core
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.run import serve_application


def run():
    _dialog_models = "models/dialog/"
    _nlu_models = "models/nlu/default/current"
    _interpreter = RasaNLUInterpreter(_nlu_models)
    _agent = Agent.load(_dialog_models, _interpreter)

    rasa_core.run.serve_application(_agent, channel='cmdline')

    return _agent


if __name__ == "__main__":
    print("Waking up the RASA console bot...")
    run()
