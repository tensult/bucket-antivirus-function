import update
import scan

def lambda_handler(event, context):
    if event != None and event.get("type", "SCAN") == "SCAN":
        return scan.lambda_handler(event, context)
    else:
        return update.lambda_handler(event, context)
