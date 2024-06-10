import mlflow
from typing import Any,Dict

def create_mlflow_experient(experiment_name:str,artifact_location:str,tags:Dict[str,Any]):
    '''
    Create a new mlflow experiment with the given name and artifact locations.
    '''
    try:
        experiment_id=mlflow.create_experiment(
            name=experiment_name,
            artifact_location=artifact_location,
            tags=tags
        )
    except:
        print(f"Experient {experiment_name} already exists.")
        experiment_id=mlflow.get_experiment_by_name(experiment_name).experiment_id
    return experiment_id

def get_mlflow_experiment(experiment_id:str=None, experiment_name:str=None):
    if experiment_id is not None:
        experiment = mlflow.get_experiment(experiment_id)
    elif experiment_name is not None:
        experiment=mlflow.get_experiment_by_name(experiment_name)
    else:
        raise ValueError("Either Experiment ID or Experiment Name must be provided.")
    return experiment


