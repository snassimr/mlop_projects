from kfp import compiler, dsl
from kfp.dsl import pipeline, component, Artifact, Dataset, Input, Metrics, Model, Output, InputPath, OutputPath


PROJECT_ID="mlops-405823"
REPOSITORY="repo1"

PIPELINE_BUCKET_NAME="gs://gcb_pipelines"
PIPELINE_ROOT = f"{PIPELINE_BUCKET_NAME}/kfp_pipeline_root/"


@component(
    base_image="us-docker.pkg.dev/mlops-405823/repo1/image_read_data",
)
def read_data(
   input_bucket_name : str, 
   input_file_name : str,
   output_dataset: OutputPath("Dataset") # Vertex AI Dataset
):
    import sys
    sys.path.append('/app/src/ds')
    from read_data import read_data

    read_data(
        input_bucket_name, 
        input_file_name, 
        output_dataset
        )

@component(
    base_image="us-docker.pkg.dev/mlops-405823/repo1/image_display_stats",
)
def display_stats(
   input_dataset: Input[Dataset], # Vertex AI Dataset
):
    import sys
    sys.path.append('/app/src/ds')
    from display_stats import display_stats

    display_stats(
        input_file_path = input_dataset.path
        )
    
@pipeline(
    pipeline_root=PIPELINE_ROOT,
    name="kfp_pipeline",
    description='Pipeline for read_data and display_stats'
)
def pipeline(
    input_bucket_name : str ,
    input_file_name : str ,
    project: str = PROJECT_ID
):

    task_read_data = read_data(
        input_bucket_name = input_bucket_name,
        input_file_name = input_file_name
        )
    
    task_display_stats = display_stats(
        input_dataset = task_read_data.output
    )

if __name__=='__main__':
    compiler.Compiler().compile(pipeline_func=pipeline, package_path="kfp_pipeline.json")

