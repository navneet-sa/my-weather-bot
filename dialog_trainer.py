# Train the rasa_core module with the training data

from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.interpreter import RasaNLUInterpreter


def train_dialog(domain_file, training_data_file, model_dir, interpreter):
    _agent = Agent(domain_file,
                   policies=[MemoizationPolicy(max_history=6),
                             KerasPolicy(
                                 MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=6),
                                 augmentation_factor=50,
                                 epochs=300,
                                 batch_size=50,
                                 validation_split=0.2
                             )],
                   interpreter=interpreter)
    _training_data = _agent.load_data(training_data_file)
    _agent.train(_training_data)
    _agent.persist(model_dir)
    return _agent


if __name__ == "__main__":
    _domain_file = "data/domain.yaml"
    _training_data_file = "data/stories.md"
    _models_dir = "models/dialog"
    _nlu_models = "models/nlu/default/current"
    _interpreter = RasaNLUInterpreter(_nlu_models)
    train_dialog(_domain_file, _training_data_file, _models_dir, _interpreter)
    print("Dialog models are generated...")
