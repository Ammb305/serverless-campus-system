## AWS Serverless Architecture

This simple architecture diagram illustrates a serverless application deployed on AWS, designed for simple serverless apps and cost-effective solutions.

![Serverless diagram](https://github.com/user-attachments/assets/6eecf32c-55e2-4318-99ee-55e8e9086b8a)


1. **Amazon CloudFront** serves the static content from **Amazon S3**.
2. **Amazon API Gateway** manages the communication between the frontend and backend, routing RESTful API requests to the **AWS Lambda** functions.
3. Lambda functions (GET and POST) handle logic and interact with **Amazon DynamoDB** to perform database operations.

Key components:
- **CloudFront**: CDN for low-latency content delivery.
- **S3**: Static file storage for the frontend.
- **API Gateway**: API management and routing.
- **Lambda**: Serverless functions for GET and POST operations.
- **DynamoDB**: NoSQL database for fast, scalable data storage.
