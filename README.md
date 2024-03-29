# k8s clustername
k8s.mikejobrien.com

# kops setup
[Getting Started with kOps on AWS](https://github.com/kubernetes/kops/blob/master/docs/getting_started/aws.md)

export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id) \
export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key) \
export NAME=k8s.mikejobrien.com \
export KOPS_STATE_STORE=s3://k8s-mikejobrien-com-state-store

# S3 bucket
aws s3api create-bucket \
    --bucket k8s-mikejobrien-com-state-store \
    --create-bucket-configuration LocationConstraint=us-west-1 \
    --region us-west-1

# Build the k8s cluster
kops update cluster ${NAME} --yes

# Delete the k8s cluster
kops delete cluster --name ${NAME} --yes    


kops create cluster \
    --zones us-west-1a \
    ${NAME}
