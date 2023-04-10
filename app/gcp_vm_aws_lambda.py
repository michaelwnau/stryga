import subprocess
import boto3
import time

def create_gcp_vm(project, zone, instance_name):
    try:
        subprocess.run(['gcloud', 'config', 'set', 'project', project], check=True)
        subprocess.run(['gcloud', 'config', 'set', 'compute/zone', zone], check=True)
        subprocess.run(['gcloud', 'compute', 'instances', 'create', instance_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating Google Cloud VM: {e}")

def delete_gcp_vm(instance_name):
    try:
        subprocess.run(['gcloud', 'compute', 'instances', 'delete', instance_name, '--quiet'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error deleting Google Cloud VM: {e}")

def execute_aws_lambda(lambda_function_name, payload):
    try:
        client = boto3.client('lambda')
        response = client.invoke(
            FunctionName=lambda_function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        return json.loads(response['Payload'].read())
    except Exception as e:
        print(f"Error executing AWS Lambda function: {e}")
        return None

def run_gcp_vm_aws_lambda(project, zone, instance_name, lambda_function_name, payload):
    create_gcp_vm(project, zone, instance_name)
    time.sleep(30)  # Wait for the VM to fully start
    lambda_response = execute_aws_lambda(lambda_function_name, payload)
    delete_gcp_vm(instance_name)
    return lambda_response

if __name__ == '__main__':
    # Example usage
    project = "your_gcp_project_id"
    zone = "your_gcp_zone"
    instance_name = "your_gcp_instance_name"
    lambda_function_name = "your_aws_lambda_function_name"
    payload = {"key": "value"}

    response = run_gcp_vm_aws_lambda(project, zone, instance_name, lambda_function_name, payload)
    print(response)
