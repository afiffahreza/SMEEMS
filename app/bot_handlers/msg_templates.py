import copy

buttonTemplate = {
    "type": "button",
    "action": {
        "type": "message",
        "label": "Placeholder",
        "text": "uuid"
    },
    "style": "primary",
    "color": "#FF735C",
    "margin": "md"
}

SMEBubbleJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Pick an SME!",
                "margin": "lg",
                "size": "xxl",
                "weight": "bold"
            }
        ],
        "spacing": "xs",
        "margin": "md",
        "alignItems": "center"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "action": {
            "type": "message",
            "label": "action",
            "text": "hello"
        }
    }
}


def createFlexBubbleSMEs(smes):
    temp = []
    for i in smes:
        tempTemplate = copy.deepcopy(buttonTemplate)

        tempTemplate["action"]["label"] = i["name"]
        tempTemplate["action"]["text"] = "smeems sme " + i["id"]

        temp.append(tempTemplate)

    SMEBubbleJSON["body"]["contents"] = temp
    return SMEBubbleJSON