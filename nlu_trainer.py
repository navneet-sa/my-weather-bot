from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

# Train the rasa_nlu with the training data and generate the ML models


# train the nlu
def train_nlu(training_data_file, nlu_config_file, model_dir):
    _training_data = load_data(training_data_file)
    _trainer = Trainer(config.load(nlu_config_file))
    _trainer.train(_training_data)

    _model_directory = _trainer.persist(model_dir, fixed_model_name="current")
    return _model_directory


if __name__ == "__main__":
    _training_data_file = "data/nlu_data.md"
    _config_file = "nlu_config.yml"
    _model_dir = "models/nlu"
    _output_dir = train_nlu(_training_data_file, _config_file, _model_dir)
    print("RASA NLU models are generated under directory: " + _output_dir)
