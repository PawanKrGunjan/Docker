import mlflow
from mlflow_utils import get_mlflow_experiment
import datetime

if __name__=="__main__":
    # create mlflow experiment
    experiment = get_mlflow_experiment(experiment_name='learning_mlflow_1')

    print("Name {}".format(experiment.name))
    print("Experiment ID: {}".format(experiment.name))
    print("Artifact location: {}".format(experiment.artifact_location))
    print("Tags:{}".format(experiment.tags))
    print("Lifecycle Stage:{}".format(experiment.lifecycle_stage))
    print('Creation timestamp: {}'.format(datetime.datetime.utcfromtimestamp(experiment.creation_time/1000)))
    print('Last updated timestamp: {}'.format(datetime.datetime.utcfromtimestamp(experiment.last_update_time/1000)))

    
