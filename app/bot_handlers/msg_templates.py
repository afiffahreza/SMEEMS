import copy

# ==================== Templates ====================

true = True #lol

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

headerTextTemplate = {
    "type": "text",
    "text": "Placeholder",
    "margin": "md",
    "weight": "bold"
}

priceTextTemplate = {
    "type": "text",
    "text": "$20",
    "margin": "md",
    "color": "#FF735C"
    }

descriptionTextTemplate = {
    "type": "text",
    "text": "This is a placeholder for the plan description hehehehehe",
    "margin": "md",
    "wrap": true
}

separatorTemplate = {
    "type": "separator",
    "margin": "lg"
}

# ==================== SME List ====================

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
                "text": "Address:",
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
                "text": "Description:",
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

# ==================== SME Plan List ====================

SMEPlanBubbleJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Placeholder",
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

def createFlexBubbleSMEPlans(sme, plans):
    temp = []
    for i in plans:
        tempHeaderTemplate = copy.deepcopy(headerTextTemplate)
        tempPriceTemplate = copy.deepcopy(priceTextTemplate)
        tempDescriptionTemplate = copy.deepcopy(descriptionTextTemplate)
        tempButtonTemplate = copy.deepcopy(buttonTemplate)

        tempHeaderTemplate["text"] = i["name"]
        tempPriceTemplate["text"] = "$" + str(i["price"])
        tempDescriptionTemplate["text"] = i["description"]

        tempButtonTemplate["action"]["label"] = "Click to Subscribe"
        tempButtonTemplate["action"]["text"] = "smeems subscribe " + i["id"]

        temp.append(tempHeaderTemplate)
        temp.append(tempPriceTemplate)
        temp.append(tempDescriptionTemplate)
        temp.append(tempButtonTemplate)
        temp.append(copy.deepcopy(separatorTemplate))

    SMEPlanBubbleJSON["hero"]["contents"][0]["text"] = sme["name"] + " Plans"
    SMEPlanBubbleJSON["body"]["contents"] = temp
    return SMEBubbleJSON