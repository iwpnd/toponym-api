# Toponym-API

API for [Toponym](https://github.com/iwpnd/toponym) built with the amazing [FastAPI](https://fastapi.tiangolo.com).

# Description

In slavic languages a word can change, depending on how and where it is used within a sentence. The city Moscow (`Москва`) changes to `Москве` when used prepositional.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

```
git clone https://github.com/iwpnd/toponym-api.git
```

```
docker build -t toponym_api .
docker run -d --name toponym-api-container -p 80:80 toponym_api
```

## Running the tests

soon

## Deployment

1. add a template.yml to the top directory containing the following and substituting \<values>:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
    Toponym API
Globals:
    Function:
        Timeout: 300
Resources:
    ToponymApiLambda:
        Type: AWS::Serverless::Function
        Properties:
            FunctionName: toponym-api-lambda
            CodeUri: toponym_api
            Handler: app.main.handler
            Runtime: python3.7
            Role: arn:aws:iam::<AWS_ACCOUNT_ID>:role/<Your Lambda Execution Role>
            Events:
                CatchAll:
                    Type: Api
                    Properties:
                        Path: /{proxy+}
                        Method: ANY
Outputs:
    ToponymApi:
      Description: "API Gateway endpoint URL for toponym-api-lambda"
      Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/prod"
    ToponymApiLambda:
      Description: "ToponymApiLambda ARN"
      Value: !GetAtt ToponymApiLambda.Arn
```

2. execute `sam build --use-container` to build your aws-sam application in a container due to C dependencies in fastapi/starlette. Use `--debug` to see whats going on.


3. You can run it locally using `sam local start-api` or you can continue and package it up to be deployed in AWS `sam package --s3-bucket <YOUR S3 BUCKET> --output-template out.yml`. This will create cloudformation template that is executed in the next step.

4. execute `sam deploy --template-file path/to/out.yml --stack-name <YOUR CLOUDFORMATION STACK NAME>`. This will deploy a stack with the toponym-api using the out.yml file to your AWS APIGateway.

5. go to your AWS console, hit APIGateway and check your API. Configurate it as you see fit, add a custom domain etcpp and deploy it in a stage.

## Authors

* **Benjamin Ramser** - *Initial work* - [iwpnd](https://github.com/iwpnd)

See also the list of [contributors](https://github.com/iwpnd/toponym/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
