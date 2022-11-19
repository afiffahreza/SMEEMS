import copy

# ==================== SME List ====================

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
        "contents": []
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

# ==================== SME Info ====================

SMEInfoBubbleJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "SME Name",
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
        "contents": [
            {
                "type": "text",
                "text": "Email:",
                "margin": "md",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "email",
                "margin": "md",
                "color": "#FF735C"
            },
            {
                "type": "text",
                "text": "Address",
                "margin": "md",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "address",
                "margin": "md",
                "color": "#FF735C"
            },
            {
                "type": "text",
                "text": "Description",
                "margin": "md",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "description",
                "color": "#FF735C",
                "margin": "md"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "Plan List",
                "text": "text"
                },
                "style": "primary",
                "color": "#FF735C",
                "margin": "lg"
            }
        ]
    }
}

def createFlexBubbleSMEInfo(sme):
    SMEInfoBubbleJSON["hero"]["contents"][0]["text"] = sme["name"]
    SMEInfoBubbleJSON["body"]["contents"][1]["text"] = sme["email"]
    SMEInfoBubbleJSON["body"]["contents"][3]["text"] = sme["address"]
    SMEInfoBubbleJSON["body"]["contents"][5]["text"] = sme["description"]
    SMEInfoBubbleJSON["body"]["contents"][6]["action"]["text"] = "smeems plans " + sme["id"]
    return SMEInfoBubbleJSON