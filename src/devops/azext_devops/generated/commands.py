# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_devops.generated._client_factory import cf_pipeline_template_definition
    devops_pipeline_template_definition = CliCommandType(
        operations_tmpl='azext_devops.vendored_sdks.devops.operations._pipeline_template_definition_operations#Pipeline'
        'TemplateDefinitionOperations.{}',
        client_factory=cf_pipeline_template_definition)
    with self.command_group('devops pipeline-template-definition', devops_pipeline_template_definition,
                            client_factory=cf_pipeline_template_definition) as g:
        g.custom_command('list', 'devops_pipeline_template_definition_list')

    from azext_devops.generated._client_factory import cf_pipeline
    devops_pipeline = CliCommandType(
        operations_tmpl='azext_devops.vendored_sdks.devops.operations._pipeline_operations#PipelineOperations.{}',
        client_factory=cf_pipeline)
    with self.command_group('devops pipeline', devops_pipeline, client_factory=cf_pipeline) as g:
        g.custom_command('list', 'devops_pipeline_list')
        g.custom_show_command('show', 'devops_pipeline_show')
        g.custom_command('create', 'devops_pipeline_create', supports_no_wait=True)
        g.custom_command('update', 'devops_pipeline_update')
        g.custom_command('delete', 'devops_pipeline_delete')
        g.wait_command('wait')
