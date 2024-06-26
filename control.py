from azureml.core import Workspace,Experiment,Environment, ScriptRunConfig

ws=Workspace.from_config()
experiment=Experiment(workspace=ws,name='Hello_world_control_experiment')

config=ScriptRunConfig(source_directory='./src',script='hello.py',compute_target='cpu-cluster')

run=experiment.submit(config)
aml_url=run.get_portal_url()
print(aml_url)