import mlflow
from mlflow_utils import create_mlflow_experient

if __name__=="__main__":
    # create mlflow experiment
    '''
    mlflow.create_experiment(
        name = 'learning_mlflow_1',
        artifact_location='D:\MLOps\mlflow\Learning\learning_mlflow_1',
        tags={'env':'dev','version':'1.0.0'}
    )
    '''
    experiment_id = create_mlflow_experient(experiment_name='learning_mlflow_1',
                                            artifact_location='D:\MLOps\mlflow\Learning\learning_mlflow_1',
                                            tags={'env':'dev','version':'1.0.0'}
                                            )

    print(f'Experiment ID:{experiment_id}')