FROM pytorch/pytorch:latest

MAINTAINER Amazon SageMaker Examples <amazon-sagemaker-examples@amazon.com>

RUN pip install pandas torchvision

COPY cifar10_pytorch.py /opt/ml/cifar10_pytorch.py
COPY core.py /opt/ml/core.py
COPY torch_backend.py /opt/ml/torch_backend.py

ENTRYPOINT ["python", "/opt/ml/cifar10_pytorch.py"]