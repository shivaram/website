Title: getting started
Slug: gettingstarted
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds
status: hidden


To get started, make sure you have an AWS account, and install pywren. You
can do the installation from either pypi

```console
$ pip install pywren
```
or from the [git repository](https://github.com/pywren/pywren/). This
installs the pywren library as well as the `pywren` command-line tool. 

### Check that your AWS credentials are setup correctly
You need to be sure you have set up your AWS creditials. 

```console
$ pywren get_aws_account_id
Your AWS account ID is 942315755674
```

Before you get started, make sure you have your AWS credentials set up 
properly for use via Boto. You also need a S3 bucket that you can write to 
to save data and retrieve results. 

Run the following from the prompt:

```console
$ pywren create_config --bucket_name YOUR_S3_BUCKET_NAME
$ pywren create_role
$ pywren deploy_lambda
```

1. This will create a default configuration file and place it in `~/.pywren_config`. 
2. Create the default IAM role to run the lambda process as `pywren_exec_role`
3. Deploy the lambda function to AWS using your account as `pywren1`. 
4. Place all intermediate data in `$YOUR_S3_BUCKET_NAME/pywren.jobs`. 


### Testing

You should now be able to run a test function . You should see the following:

```console
$ pywren test_function

function returned: Hello world
```

### Next steps
Check out [the examples](https://github.com/pywren/examples)


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
