Title: PyWren 0.1
Date: 2017-03-06
Tags: releases
Category: releases
Slug: release-0.1
Author: Eric Jonas
Summary: Annoucing PyWren 0.1, with Python 3 support, large-scale reducers, better logging, support for running on arbitray instances, and a new website! 

Today we're excited to annouce the latest version of PyWren, version 0.1. This
is our first release with a stand-alone mode, a `reduce` verb, and Python 3 support. 
A lot has happened over the past few months with PyWren. There was a a
talk AnacondaCon and we
were
[written up at the the New Stack](https://thenewstack.io/aws-lambda-finds-unexpected-market-scientific-computing/).
We posted our latest paper on the
arXiv,
[Occupy the Cloud: Distributed Computing for the 99%](https://arxiv.org/abs/1702.04024). We
[moved the project to a github organization](https://github.com/pywren/) and
split off
and [organized the examples](https://github.com/pywren/examples).

## Stand-alone mode

We sometimes run into situations where we can't get around Lambda's
limits of runtime and memory, or need a GPU, or want to run our code
on a machine with 2 TB of RAM. We created a new type of executor,
`standalone`, which runs PyWren jobs inside our Anaconda runtime on
arbitrary EC2 instances, using Amazon's SQS as a queue dispatch
system.  Jobs can run for up to 12 hours, and the available memory is
constrained only by the instance type. When the queue is empty, the
instance will shut itself down automatically.

Note that this feature is still somewhat experimental, and
we're actively soliciting feedback. We'll have a complete
example of use soon. 

## Reduce 

Up till now, PyWren has largely supported `map`-like
functionality. Many machine-learning workloads consist of a
featurization step that is embarrassingly parallel, followd by a large
distributed machine-learning operation that aggregates the result of
that featurization.

Enter `reduce`. Now you can write

```python
lexec = pywren.lambda_executor()
sexec = pywren.standalone_executor()

features = lexec.map(create_feature, data)
model = sexec.reduce(train_model, features)
```

The benefit here is the standalone executor can be one of the massive
AWS instances, like the `x1.32xlarge`, with 2 TB of ram and 64 cores. Even
if training your model takes an hour, it's only $14. 

This functionality is also experimental, and we'll have a good
example soon! 

## Python 3 support
Based on great work by [@washcycle](https://github.com/washcycle), we now have
full Python 3 support and Python 3.5 and 3.6 are fully-supported runtimes. 

## Other improvements:

* New website, [pywren.io](http://pywren.io)
* Additional contributors, especially [Qifan Pu](https://people.eecs.berkeley.edu/~qifan/) and [Shivaram Venkataraman](http://shivaram.org/), and support from both the Berkeley Center for Computational Imaging (via [Ben Recht](https://people.eecs.berkeley.edu/~brecht/)) and the [UC Berkeley RISE Lab ](https://rise.cs.berkeley.edu/) (thanks to [Ion Stoica](https://people.eecs.berkeley.edu/~istoica/) ) 
* Installable via PyPi
* Improved error handling and catching of exceptions


