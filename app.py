from aws_cdk import core

from cdk_ecs_example.cdk_ecs_example_stack import CdkEcsExampleStack

app = core.App()
CdkEcsExampleStack(app, "CdkEcsExample")

app.synth()
