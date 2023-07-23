## API Deployment on Kubernetes

This is an API WebApp deployment on Kubernetes

### API deployment project description

Simple API is a simple application conformed of 3 services, the api-external, the api-month, and the api-day. The api-external is the entry point and needs to be exposed outside the cluster via the URL https://api-external.dev through it you can invoke the 2 services api-month and api-day that print the day of the week and the month in their respective logs. 

The API call is secured using a secret in the headers.
The endpoints(ENDPOINT_DAY, ENDPOINT_MONTH), ports(PORT), and secret(API_SECRET) must be configured in each Kubernetes deployment through environment variables. 
Use configmaps and secrets according to the variable type.

### Tips

  1.	You can use minikube to test your work.
  2.	Components can have bugs, they're simple, so it shouldn't take long to figure it out.
  3. 	You can deploy fluentbit or filebeat and a single Elasticsearch instance without Kibana, we can view the logs through Elasticsearch REST API.

### To-do

  1.	Clone this repository
  2.	Create a new dev branch
  3.	Please, make sure you use as many commits as possible. We would love to see your progress
  4.	create a Pull Request to master
  5.	Be ready to answer questions

### Requirements

  1.	Keep a clean and understandable folder structure.
  2.	Document your work, we love comments and documentation.
  3.	Write all the documentation and comments in English.
  4.	Use docker and Kubernetes.

### Your tasks:

  1.	Deploy the services set from the repository to production env using Kubernetes.
  2.	Configure a simple Kubernetes cronjob that calls both api endpoints every day at 1:00 am.
  3.	Send component logs to an Elasticsearch instance deployed in the cluster.

### Evaluation criteria

  1. The deployment flow has to run, please provide short setup instructions.
  2. Security.
  3. Automation.
  4. Liveness and Readiness of each dependent service.
  5. Usage of Docker and Kubernetes.

