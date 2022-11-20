import copy
from app.services.smes import get_sme
from app.services.plans import get_plan

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

inactivePlanTemplate = {
    "type": "box",
    "layout": "vertical",
    "contents": [
        {
        "type": "text",
        "text": "Subscription name",
        "margin": "md",
        "weight": "bold"
        },
        {
        "type": "text",
        "text": "SME Name",
        "margin": "md",
        "color": "#FF735C"
        },
        {
        "type": "text",
        "text": "This is a placeholder for the plan description that the user has",
        "margin": "md",
        "wrap": true
        },
        {
        "type": "button",
        "action": {
            "type": "message",
            "label": "Pay to Activate",
            "text": "text"
        },
        "style": "primary",
        "color": "#FF735C",
        "margin": "lg"
        }
    ]
}

activePlanTemplate = {
    "type": "box",
    "layout": "vertical",
    "contents": [
        {
        "type": "text",
        "text": "Basic Plan",
        "margin": "md",
        "weight": "bold"
        },
        {
        "type": "text",
        "text": "Hi Brew Coffee",
        "margin": "md",
        "color": "#FF735C"
        },
        {
        "type": "text",
        "text": "Free 15% off for all drinks",
        "margin": "md",
        "wrap": true
        },
        {
        "type": "box",
        "layout": "horizontal",
        "contents": [
            {
            "type": "text",
            "text": "Active until",
            "align": "start",
            "color": "#0c9905",
            "weight": "bold"
            },
            {
            "type": "text",
            "text": "12-12-2022",
            "align": "end"
            }
        ],
        "margin": "md",
        "alignItems": "flex-start",
        "justifyContent": "flex-start"
        }
    ]
}

expiredPlanTemplate = {
    "type": "box",
    "layout": "vertical",
    "contents": [
        {
        "type": "text",
        "text": "Gold Plan",
        "margin": "md",
        "weight": "bold"
        },
        {
        "type": "text",
        "text": "Peza Pizza",
        "margin": "md",
        "color": "#FF735C"
        },
        {
        "type": "text",
        "text": "Free 15% off for all drinks",
        "margin": "md",
        "wrap": true
        },
        {
        "type": "text",
        "text": "Expired",
        "margin": "md",
        "align": "start",
        "color": "#FF0000",
        "weight": "bold"
        },
        {
        "type": "button",
        "action": {
            "type": "message",
            "label": "Pay to Renew",
            "text": "text"
        },
        "style": "primary",
        "color": "#FF735C",
        "margin": "lg"
        },
        {
        "type": "text",
        "text": "OR",
        "margin": "md",
        "wrap": true,
        "align": "center"
        },
        {
        "type": "button",
        "action": {
            "type": "message",
            "label": "Remove Subscription",
            "text": "text"
        },
        "style": "primary",
        "color": "#FF735C",
        "margin": "lg"
        }
    ]
}

# ==================== Success Messages ====================

successJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
        {
            "type": "image",
            "url": "https://cdn-icons-png.flaticon.com/512/845/845646.png",
            "size": "30px"
        },
        {
            "type": "text",
            "text": "Success",
            "margin": "lg",
            "size": "20px",
            "weight": "bold"
        },
        {
            "type": "image",
            "url": "https://cdn-icons-png.flaticon.com/512/845/845646.png",
            "size": "30px"
        }
        ],
        "spacing": "xs",
        "margin": "lg",
        "alignItems": "center",
        "justifyContent": "center",
        "paddingAll": "10px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Success Message",
            "wrap": true
        }
        ]
    }
}

def createFlexBubbleSuccess(success):
    successJSON["body"]["contents"][0]["text"] = success
    return successJSON

# ==================== Warning Messages ====================

errorJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
        {
            "type": "image",
            "url": "https://cdn-icons-png.flaticon.com/512/3756/3756712.png",
            "size": "40px"
        },
        {
            "type": "text",
            "text": "Warning",
            "margin": "lg",
            "size": "20px",
            "weight": "bold"
        },
        {
            "type": "image",
            "url": "https://cdn-icons-png.flaticon.com/512/3756/3756712.png",
            "size": "40px"
        }
        ],
        "spacing": "xs",
        "margin": "lg",
        "alignItems": "center",
        "justifyContent": "center",
        "paddingAll": "10px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Error Message",
            "wrap": true
        }
        ]
    }
}

def createFlexBubbleError(error):
    errorJSON["body"]["contents"][0]["text"] = error
    return errorJSON

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
    for i, data in enumerate(plans):
        tempHeaderTemplate = copy.deepcopy(headerTextTemplate)
        tempPriceTemplate = copy.deepcopy(priceTextTemplate)
        tempDescriptionTemplate = copy.deepcopy(descriptionTextTemplate)
        tempButtonTemplate = copy.deepcopy(buttonTemplate)

        tempHeaderTemplate["text"] = data["name"]
        tempPriceTemplate["text"] = "$" + str(data["price"])
        tempDescriptionTemplate["text"] = data["description"]

        tempButtonTemplate["action"]["label"] = "Click to Subscribe"
        tempButtonTemplate["action"]["text"] = "smeems subscribe " + data["id"]

        temp.append(tempHeaderTemplate)
        temp.append(tempPriceTemplate)
        temp.append(tempDescriptionTemplate)
        temp.append(tempButtonTemplate)

        # if not last element append separator
        if i != len(plans) - 1:
            temp.append(separatorTemplate)

    SMEPlanBubbleJSON["hero"]["contents"][0]["text"] = sme["name"] + " Plans"
    SMEPlanBubbleJSON["body"]["contents"] = temp
    return SMEPlanBubbleJSON

# ==================== Subscription List ====================
SubscriptionBubbleJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Your Subscription",
            "size": "xxl",
            "weight": "bold",
            "margin": "lg"
        }
        ],
        "alignItems": "center"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": []
    }
}

def createFlexBubbleSubscriptionList(subscriptions):
    temp = []
    for i, data in enumerate(subscriptions):

        # get plan info from data["plan_id"]
        plan = get_plan(data["plan_id"])
        # get sme name from plan["sme_id"]
        sme = get_sme(plan["sme_id"])

        if data["status"] == "active":
            tempActiveTemplate = copy.deepcopy(activePlanTemplate)
            tempActiveTemplate["contents"][0]["text"] = plan["name"]
            tempActiveTemplate["contents"][1]["text"] = sme["name"]
            tempActiveTemplate["contents"][2]["text"] = plan["description"]
            tempActiveTemplate["contents"][3]["contents"][1]["text"] = data["end_date"]

            temp.append(tempActiveTemplate)

        elif data["status"] == "inactive":
            tempInactiveTemplate = copy.deepcopy(inactivePlanTemplate)
            tempInactiveTemplate["contents"][0]["text"] = plan["name"]
            tempInactiveTemplate["contents"][1]["text"] = sme["name"]
            tempInactiveTemplate["contents"][2]["text"] = plan["description"]

            # change button
            tempInactiveTemplate["contents"][3]["action"]["text"] = "smeems pay " + data["id"]

            temp.append(tempInactiveTemplate)

        elif data["status"] == "expired":
            tempExpiredTemplate = copy.deepcopy(expiredPlanTemplate)
            tempExpiredTemplate["contents"][0]["text"] = plan["name"]
            tempExpiredTemplate["contents"][1]["text"] = sme["name"]
            tempExpiredTemplate["contents"][2]["text"] = plan["description"]

            # change button
            tempExpiredTemplate["contents"][4]["action"]["text"] = "smeems pay " + data["id"]
            tempExpiredTemplate["contents"][6]["action"]["text"] = "smeems unsubscribe " + data["id"]


            temp.append(tempExpiredTemplate)

        # if not last element append separator
        if i != len(subscriptions) - 1:
            temp.append(separatorTemplate)

    SubscriptionBubbleJSON["body"]["contents"] = temp
    return SubscriptionBubbleJSON