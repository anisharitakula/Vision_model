import azureml.core
from azureml.core.compute import AmlCompute
from azureml.core.compute import ComputeTarget

from azureml.core import Workspace,Experiment
#from azureml.core.authentication import InteractiveLoginAuthentication

#forced_interactive_auth = InteractiveLoginAuthentication(tenant_id="ef766168-b150-4c78-ac02-88f61847b5a2", force=True)

ws=Workspace.from_config()

amlcompute_cluster_name="cpu-cluster"

provisioning_config=AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2',
                                                          min_nodes=0,max_nodes=4)
compute_target=ComputeTarget.create(ws,amlcompute_cluster_name,provisioning_config)

compute_target.wait_for_completion(show_output=True,min_node_count=None,timeout_in_minutes=20)

print("reached the end")