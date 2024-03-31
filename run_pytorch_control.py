from azureml.core import Workspace,Experiment,Environment,ScriptRunConfig

if __name__=="__main__":
    ws=Workspace.from_config()
    experiment=Experiment(workspace=ws,name='CIFAR_train_run_v1')
    config=ScriptRunConfig(source_directory='./src',script='train.py',
                           compute_target='cpu-cluster')
    
    #set up pytorch environment
    env=Environment.from_conda_specification(name='pytorch-env',file_path=
                                             'pytorch-env.yml')
    config.run_config.environment=env

    run=experiment.submit(config)
    aml_url=run.get_portal_url()
    print(aml_url)