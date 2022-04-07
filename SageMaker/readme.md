# Sagemaker Auto-pilot

<img src="https://user-images.githubusercontent.com/34656794/162124612-db897640-542f-46b7-ace7-f4b49ae69e0a.png" data-canonical-src="https://user-images.githubusercontent.com/34656794/162124612-db897640-542f-46b7-ace7-f4b49ae69e0a.png" width="750" height="250">

The steps followed in this phase is as follows:  
1- Log into AWS account  
2- Create a new Sagemaker jupyter notebook (which will create a default S3 bucket associated to it)    
<img src="https://user-images.githubusercontent.com/34656794/162125588-9b3a71a6-fb44-4fd7-b5d8-f443638487ec.png" width="400" height="250">

3- The jupyter notebook (Test_data.ipynb) contains the code to install Kaggle package, download the data from kaggle API, split the data and configure the sagemaker autopilot job.  
4- Once the auto-pilot job is completed, we end up having the best model and then we tracked and analyzed the jobs created in sage maker:  
<img src="https://user-images.githubusercontent.com/34656794/162125813-712b9b02-488e-4e82-96d9-fcf58a23795a.png" width="450" height="250">  
5- Next step was to create an end-point to this model in oder to be able to expose it externally in the next steps.  
![image](https://user-images.githubusercontent.com/34656794/162126519-24940578-d994-4acb-a08d-edc9d88a7feb.png)  
6- With the endpoint up and running we will then create a lambda function that will point to the model endpoint (code attached).  
7- After the lambda function completion we will configure the API gateway to add a new API that is pointing to the Lambda function.  
7.1 This is done by first creating a resource.   
7.2 Create a POST method under this resource and pick Lambda function.  
7.3 Configure the API the way you want (i.e. with API key or no).  
7.4 Create a stage.  
7.5 Deploy the API.  





