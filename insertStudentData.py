import json
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Use the DynamoDB object to select our table
table = dynamodb.Table('studentData')

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # Extract values from the event object we got from the Lambda service and store in variables
    student_id = event.get('StudentID')  # Use get to avoid KeyError if key is missing
    name = event.get('name')
    student_year = event.get('year')
    age = event.get('age')
    
    # Check if all required fields are present
    if not all([student_id, name, student_year, age]):
        return {
            'statusCode': 400,
            'body': json.dumps('Missing one or more required parameters.')
        }
    
    try:
        # Write student data to the DynamoDB table
        response = table.put_item(
            Item={
                'StudentID': student_id,
                'name': name,
                'year': student_year,
                'age': age
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Student data saved successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error saving data: {str(e)}')
        }
