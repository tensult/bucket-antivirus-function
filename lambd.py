import update
import scan

def lambda_handler(event, context):
    if event == None or event.get("type", "UPDATE") == "UPDATE":
        return update.lambda_handler(event, context)
    else:
        return scan.lambda_handler(event, context)
