# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class AzureDevOpsScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_devops_myAspNetWebAppPipeline-rg'[:9], key='rg')
    def test_devops(self, resource_group):

        self.kwargs.update({
            'myAspNetWebAppPipeline': self.create_random_name(prefix='cli_test_pipelines'[:9], length=24),
        })

        # EXAMPLE: Pipelines/resource-group-name/Create an Azure pipeline to deploy a sample ASP.Net application to Azure web-app
        self.cmd('az devops pipeline create '
                 '--location "South India" '
                 '--bootstrap-configuration "{{\\"template\\":{{\\"id\\":\\"ms.vss-continuous-delivery-pipeline-templat'
                 'es.aspnet-windowswebapp\\",\\"parameters\\":{{\\"appInsightLocation\\":\\"South India\\",\\"appServic'
                 'ePlan\\":\\"S1 Standard\\",\\"azureAuth\\":\\"{{\\\\\\"scheme\\\\\\":\\\\\\"ServicePrincipal\\\\\\",'
                 '\\\\\\"parameters\\\\\\":{{\\\\\\"tenantid\\\\\\":\\\\\\"{{subscriptionTenantId}}\\\\\\",\\\\\\"objec'
                 'tid\\\\\\":\\\\\\"{{appObjectId}}\\\\\\",\\\\\\"serviceprincipalid\\\\\\":\\\\\\"{{appId}}\\\\\\",\\'
                 '\\\\"serviceprincipalkey\\\\\\":\\\\\\"{{appSecret}}\\\\\\"}}}}\\",\\"location\\":\\"South India\\",'
                 '\\"resourceGroup\\":\\"myAspNetWebAppPipeline-rg\\",\\"subscriptionId\\":\\"{{subscriptionId}}\\",\\"'
                 'webAppName\\":\\"myAspNetWebApp\\"}}}}}}" '
                 '--organization name=myAspNetWebAppPipeline-org '
                 '--project name=myAspNetWebAppPipeline-project '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline show '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline update '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}" '
                 '--tags tagKey=tagvalue',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline delete '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/List all Azure Pipelines under the specified resource group
        self.cmd('az devops pipeline list '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/api-version/List all Azure pipelines under the specified subscription
        self.cmd('az devops pipeline list',
                 checks=[])

        # EXAMPLE: PipelineTemplateDefinitions/api-version/Get the list of pipeline template definitions
        self.cmd('az devops pipeline-template-definition list',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline show '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline update '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}" '
                 '--tags tagKey=tagvalue',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline delete '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline show '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline update '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}" '
                 '--tags tagKey=tagvalue',
                 checks=[])

        # EXAMPLE: Pipelines/resource-group-name/Get an existing Azure pipeline
        self.cmd('az devops pipeline delete '
                 '--pipeline-name "{myAspNetWebAppPipeline}" '
                 '--resource-group "{rg}"',
                 checks=[])
