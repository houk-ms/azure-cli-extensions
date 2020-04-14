# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def devops_pipeline_template_definition_list(cmd, client):
    return client.list()


def devops_pipeline_list(cmd, client,
                         resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def devops_pipeline_show(cmd, client,
                         resource_group_name,
                         pipeline_name):
    return client.get(resource_group_name=resource_group_name,
                      pipeline_name=pipeline_name)


def devops_pipeline_create(cmd, client,
                           resource_group_name,
                           pipeline_name,
                           organization,
                           project,
                           bootstrap_configuration,
                           tags=None,
                           location=None):
    if isinstance(bootstrap_configuration, str):
        bootstrap_configuration = '{\
            "template": {\
                "id": "ms.vss-continuous-delivery-pipeline-templates.aspnet-windowswebapp",\
                "parameters": {\
                    "appInsightLocation": "South India",\
                    "appServicePlan": "S1 Standard",\
                    "location": "South India",\
                    "resourceGroup": "myAspNetWebAppPipeline-rg",\
                    "subscriptionId": "0b1f6471-1bf0-4dda-aec3-cb9272f09590",\
                    "webAppName": "myAspNetWebApp"\
                }\
            }\
        }'
        bootstrap_configuration = json.loads(bootstrap_configuration)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         pipeline_name=pipeline_name,
                                         tags=tags,
                                         location=location,
                                         organization=organization,
                                         project=project,
                                         bootstrap_configuration=bootstrap_configuration)


def devops_pipeline_update(cmd, client,
                           resource_group_name,
                           pipeline_name,
                           tags=None):
    return client.update(resource_group_name=resource_group_name,
                         pipeline_name=pipeline_name,
                         tags=tags)


def devops_pipeline_delete(cmd, client,
                           resource_group_name,
                           pipeline_name):
    return client.delete(resource_group_name=resource_group_name,
                         pipeline_name=pipeline_name)
