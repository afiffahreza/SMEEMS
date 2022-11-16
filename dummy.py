contentTemplate = {
    "type": "button",
    "action": {
        "type": "message",
        "label": "Placeholder",
        "text": "uuid"
    },
    "style": "primary",
    "color": "#FF735C"
}

bubbleJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Pick a SME!",
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


testData = [
    {
        "id": "1",
        "name": "test"
    },
    {
        "id": "2",
        "name": "kedua"
    },
    {
        "id": "3",
        "name": "ketiga"
    },
]

def testAppend():
    test = []
    for i in range(3):
        tes = str(i)
        test.append(tes)
    print(test)
# testAppend()

def createFlexBubbleSMEs():
    temp = []
    for i in testData:
        tempTemplate = contentTemplate
        tempTemplate["action"]["label"] = i["name"]
        tempTemplate["action"]["text"] = i["id"]
        
        temp.append(tempTemplate)
        
        print(temp)
        print("")
        print(tempTemplate)

    bubbleJSON["body"]["contents"] = temp
    print("\n\ntes\n\n", bubbleJSON["body"]["contents"])


createFlexBubbleSMEs()
