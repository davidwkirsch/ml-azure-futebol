from azureml.core import Workspace, Experiment
from azureml.train.automl import AutoMLConfig

# Connect to your workspace
ws = Workspace.from_config()

# Define your experiment
experiment = Experiment(ws, 'football_game_prediction')

# Configure AutoML settings
automl_settings = {
    "task": "classification",
    "primary_metric": "accuracy",
    "experiment_timeout_minutes": 60,
    "max_concurrent_iterations": 4,
    "max_cores_per_iteration": -1,
    "featurization": "auto",
    "verbosity": logging.INFO,
    "n_cross_validations": 5,
    "enable_early_stopping": True
}

# Define AutoML configuration
automl_config = AutoMLConfig(
    training_data=train_data,
    label_column_name="winner",
    **automl_settings
)

# Submit the experiment
run = experiment.submit(automl_config, show_output=True)
