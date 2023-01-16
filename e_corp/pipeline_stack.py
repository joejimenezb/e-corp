from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import (
    Stack
)

class AWSomePipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Pipeline code will go here

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="E-Corp_Pipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("joejimenezb/e-corp", "main"),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )