import argparse
import json

def get_bprintApi_request():
    parser = argparse.ArgumentParser()

    #Adding arguements
    parser.add_argument("-request_payload", "--request_payload")
    args = parser.parse_args()

    blueprint_request = {
        "request_payload": json.loads(args.request_payload)
    }
    print(blueprint_request) 


if __name__=="__main__":
    get_bprintApi_request()

# python userArg.py -request_payload="{\"template_id\": \"603de958ab8d5845f03f5dd3\"}"