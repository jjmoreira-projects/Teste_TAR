import requests
import xml.etree.ElementTree as ET

response = requests.get("http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa")
root = ET.fromstring(response.content)
print(root.text)

