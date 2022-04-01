import argparse
import json

def get_bprintApi_request():
    parser = argparse.ArgumentParser()

    #Adding arguements
    parser.add_argument("-request_payload", "--request_payload")
    args = parser.parse_args()

    # print("\nargs: "+ str(args))

    blueprint_request = {
        "request_payload": json.loads(args.request_payload)
    }
    print("\nReceived request payload:")
    print(blueprint_request['request_payload']) 

    # print(blueprint_request) 



if __name__=="__main__":
    get_bprintApi_request()

# python userArg.py -request_payload="{\"template_id\": \"603de958ab8d5845f03f5dd3\"}"
# python userArg.py -request_payload="{\"template_id\": \"603de958ab8d5845f03f5dd3\",\"payload\": {\"name\": \"aws_vpc_py0\",\"vpc_cidr_block\": \"10.0.0.0/16\",\"public_subnet_cidr_block\": \"10.0.0.0/24\",\"private_subnet_cidr_block\": \"10.0.1.0/24\",\"cloud_accounts\":[{\"cloud_account_id\": \"619f2c0407e832aefe019e3a\",\"region\": \"ap-south-1\"}]}}"
# python userArg.py -h