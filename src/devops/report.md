# Azure CLI Module Creation Report

### devops pipeline create

create a devops pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resource_group_name|
|**--pipeline_name**|string|The name of the Azure Pipeline resource in ARM.|pipeline_name|pipeline_name|
|**--organization**|object|Reference to the Azure DevOps Organization containing the Pipeline.|organization|organization|
|**--project**|object|Reference to the Azure DevOps Project containing the Pipeline.|project|project|
|**--bootstrap_configuration**|object|Configuration used to bootstrap the Pipeline.|bootstrap_configuration|bootstrap_configuration|
|**--tags**|dictionary|Resource Tags|tags|tags|
|**--location**|string|Resource Location|location|location|
### devops pipeline delete

delete a devops pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resource_group_name|
|**--pipeline_name**|string|The name of the Azure Pipeline resource.|pipeline_name|pipeline_name|
### devops pipeline list

list a devops pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resource_group_name|
### devops pipeline show

show a devops pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resource_group_name|
|**--pipeline_name**|string|The name of the Azure Pipeline resource in ARM.|pipeline_name|pipeline_name|
### devops pipeline update

update a devops pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resource_group_name|
|**--pipeline_name**|string|The name of the Azure Pipeline resource.|pipeline_name|pipeline_name|
|**--tags**|dictionary|Dictionary of key-value pairs to be set as tags on the Azure Pipeline. This will overwrite any existing tags.|tags|tags|
### devops pipeline-template-definition list

list a devops pipeline-template-definition.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|