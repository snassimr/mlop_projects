from google.cloud import aiplatform

INPUT_BUCKET_NAME="gcb_input"
INPUT_FILE_NAME="adult.csv"

if __name__ == '__main__':

    from datetime import datetime
    current_timestamp = datetime.now()
    job_id_timestamp = current_timestamp.strftime("d-%Y-%m-%d-t-%H-%M-%S")

    run = aiplatform.PipelineJob(
        display_name="kfp-pipeline-run-job",
        template_path="kfp_pipeline.json",
        job_id=f"kfp-pipeline-run-job-{job_id_timestamp}",
        parameter_values = {
            "input_bucket_name": INPUT_BUCKET_NAME,
            "input_file_name": INPUT_FILE_NAME
            },
        enable_caching=False,)

    run.submit()