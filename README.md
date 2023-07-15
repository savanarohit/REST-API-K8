# api-k8-deployment
Simple API-based application deployment on Kubernetes

## Simple API project description

Simple API is a simple application conformed of 3 services, the api-external, the api-month, and the api-day. The api-external is the entry point and needs to be exposed outside the cluster via the URL https://api-external.dev through it you can invoke the 2 services api-month and api-day that simply print the day of the week and the month in their respective logs. The API call is secured using a secret in the headers.
The endpoints(ENDPOINT_DAY, ENDPOINT_MONTH), ports(PORT), and secret(API_SECRET) must be configured in each Kubernetes deployment through environment variables. Use configmaps and secrets according to the variable type.

## Tip

1.	You can use minikube to test your work.
2.	Components can have bugs, they're simple, so it shouldn't take long to figure it out.
3. 	You can deploy fluentbit or filebeat and a single Elasticsearch instance without Kibana, we can view the logs through Elasticsearch REST API.

## To-do

1.	Clone this repository
2.	Create a new dev branch
3.	Please, make sure you use as many commits as possible. We would love to see your progress
4.	create a Pull Request to master
5.	Be ready to answer questions

## Evaluation criteria

This is what we look at - among other things:
•	The deployment flow has to run, please provide short setup instructions.
•	Security.
•	Automation.
•	Liveness and Readiness of each dependent service.
•	Usage of Docker and Kubernetes.

