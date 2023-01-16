#!/usr/bin/env python3

import aws_cdk as cdk

from e_corp.e_corp_stack import ECorpStack
from e_corp.pipeline_stack import AWSomePipelineStack


app = cdk.App()
ECorpStack(app, "e-corp")
AWSomePipelineStack(app, "AWSomePipelineStack", 
    env=cdk.Environment(account="069320687453", region="us-east-1")
)

app.synth()
