import requests
from typing import Dict, Optional


class MetaTemplateSender:
    def __init__(self, access_token: str, business_account_id: str, graph_version: str ):
        self.access_token = access_token
        self.business_account_id = business_account_id
        self.graph_version = graph_version
        self.api_url = f"https://graph.facebook.com/{self.graph_version}/{self.business_account_id}/message_templates"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def build_payload(self, data: Dict) -> Dict:
        payload = {
            "name": data["template_name"],
            "category": data["category"],
            "language": data["language"],
            "components": []
        }

        if "header" in data and data["header"]:
            payload["components"].append({
                "type": "HEADER",
                "format": "TEXT",
                "text": data["header"]
            })

        payload["components"].append({
            "type": "BODY",
            "text": data["body"]
        })

        if "footer" in data and data["footer"]:
            payload["components"].append({
                "type": "FOOTER",
                "text": data["footer"]
            })

        return payload

    def send_template(self, data: Dict) -> Dict:
        payload = self.build_payload(data)
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            if response.status_code == 200:
                return {"status": "creado", "template": data["template_name"]}
            else:
                return {
                    "status": "error",
                    "template": data["template_name"],
                    "meta_response": response.json()
                }
        except Exception as e:
            return {
                "status": "error",
                "template": data["template_name"],
                "exception": str(e)
            }