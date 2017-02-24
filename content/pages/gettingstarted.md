Title: getting started
Slug: gettingstarted
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds
status: hidden


To get started, make sure you have an AWS account, and install pywren.

```
pip install pywren
```

### Check that your AWS credentials are setup correctly

```
pywren aws_check
```

### Walk through setup script


### First example


### When things go wrong

1. getting the logs

2. filing an issue

3. 


## Getting started

First, make sure you have boto set up to use your AWS credentials and
have a sane python installation (I recommend [Anaconda](https://www.continuum.io/downloads )). Clone the repo from git and invoke:

```
python setup.py install
```

Before you get started, make sure you have your AWS credentials set up 
properly for use via Boto. You also need a s3 bucket that you can write to 
to save data and retrieve results. 

Run the following from the prompt:

```
pywren create_config --bucket_name YOUR_S3_BUCKET_NAME
pywren create_role
pywren deploy_lambda
```

1. This will create a default configuration file and place it in `~/.pywren_config`. 
2. Create the default IAM role to run the lambda process as `pywren_exec_role`
3. Deploy the lambda function to AWS using your account as `pywren1`. 
4. Place all intermediate data in `$YOUR_S3_BUCKET_NAME/pywren.jobs`. 


### Testing

You should now be able to run `examples/simpletest.py`. You should see the following:

```
# python examples/simpletest.py
# Linux ip-10-13-24-185 4.4.19-29.55.amzn1.x86_64 #1 SMP Mon Aug 29 23:29:40 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

## Debugging (When things go wrong)

Pywren will print logging info to console by setting the environment
varible as follows:

```
PYWREN_LOGLEVEL=INFO
```

Logs are written to AWS Cloudwatch. To print the latest cloudwatch from the commandline use:
```
pywren print_latest_logs
```

To inspect the logs through the AWS GUI get the URL for the current worker
via 
```
pywren log_url
```
